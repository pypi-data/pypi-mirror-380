"""
Dakora Playground Server

A FastAPI server that provides a web-based playground for creating,
editing, and testing prompt templates in real-time.
"""

from __future__ import annotations
import json
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
import uvicorn

from .vault import Vault
from .model import TemplateSpec, InputSpec
from .exceptions import TemplateNotFound, ValidationError, RenderError


class RenderRequest(BaseModel):
    inputs: Dict[str, Any] = Field(default_factory=dict)


class CreateTemplateRequest(BaseModel):
    id: str
    version: str = "1.0.0"
    description: Optional[str] = None
    template: str
    inputs: Dict[str, Dict[str, Any]] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class UpdateTemplateRequest(BaseModel):
    version: Optional[str] = None
    description: Optional[str] = None
    template: Optional[str] = None
    inputs: Optional[Dict[str, Dict[str, Any]]] = None
    metadata: Optional[Dict[str, Any]] = None


class TemplateResponse(BaseModel):
    id: str
    version: str
    description: Optional[str]
    template: str
    inputs: Dict[str, Any]
    metadata: Dict[str, Any]


class RenderResponse(BaseModel):
    rendered: str
    inputs_used: Dict[str, Any]


class PlaygroundServer:
    def __init__(self, vault: Vault, host: str = "localhost", port: int = 3000):
        self.vault = vault
        self.host = host
        self.port = port
        self.app = self._create_app()

    def _create_app(self) -> FastAPI:
        app = FastAPI(
            title="Dakora Playground",
            description="Interactive playground for prompt template development",
            version="0.1.0"
        )

        # API Routes
        @app.get("/api/templates", response_model=List[str])
        async def list_templates():
            """List all available template IDs."""
            try:
                return list(self.vault.list())
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @app.get("/api/templates/{template_id}", response_model=TemplateResponse)
        async def get_template(template_id: str):
            """Get a specific template with all its details."""
            try:
                template = self.vault.get(template_id)
                spec = template.spec
                return TemplateResponse(
                    id=spec.id,
                    version=spec.version,
                    description=spec.description,
                    template=spec.template,
                    inputs={name: {
                        "type": input_spec.type,
                        "required": input_spec.required,
                        "default": input_spec.default
                    } for name, input_spec in spec.inputs.items()},
                    metadata=spec.metadata
                )
            except TemplateNotFound:
                raise HTTPException(status_code=404, detail=f"Template '{template_id}' not found")
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @app.post("/api/templates", response_model=TemplateResponse)
        async def create_template(request: CreateTemplateRequest):
            """Create a new template and save it to the filesystem."""
            try:
                # Validate request
                if not request.id or request.id.strip() == "":
                    raise HTTPException(status_code=422, detail="Template ID cannot be empty")

                # Check if template already exists
                try:
                    self.vault.get(request.id)
                    raise HTTPException(status_code=400, detail=f"Template '{request.id}' already exists")
                except TemplateNotFound:
                    pass  # Template doesn't exist, which is what we want

                # Convert input specs from dict format to InputSpec objects
                inputs_dict = {}
                for input_name, input_data in request.inputs.items():
                    inputs_dict[input_name] = InputSpec(
                        type=input_data.get("type", "string"),
                        required=input_data.get("required", True),
                        default=input_data.get("default")
                    )

                # Create TemplateSpec object and validate it
                spec = TemplateSpec(
                    id=request.id,
                    version=request.version,
                    description=request.description,
                    template=request.template,
                    inputs=inputs_dict,
                    metadata=request.metadata
                )

                # Save template to YAML file
                prompt_dir = Path(self.vault.config["prompt_dir"])
                filename = f"{spec.id}.yaml"
                file_path = prompt_dir / filename

                # Create the YAML content
                yaml_content = {
                    "id": spec.id,
                    "version": spec.version,
                    "description": spec.description,
                    "template": spec.template,
                    "inputs": {
                        name: {
                            "type": input_spec.type,
                            "required": input_spec.required,
                            "default": input_spec.default
                        }
                        for name, input_spec in spec.inputs.items()
                    },
                    "metadata": spec.metadata
                }

                # Write to file
                with open(file_path, 'w', encoding='utf-8') as f:
                    yaml.dump(yaml_content, f, default_flow_style=False, sort_keys=False)

                # Invalidate cache to pick up the new template
                self.vault.invalidate_cache()

                # Return the created template
                return TemplateResponse(
                    id=spec.id,
                    version=spec.version,
                    description=spec.description,
                    template=spec.template,
                    inputs={name: {
                        "type": input_spec.type,
                        "required": input_spec.required,
                        "default": input_spec.default
                    } for name, input_spec in spec.inputs.items()},
                    metadata=spec.metadata
                )

            except HTTPException:
                raise  # Re-raise HTTP exceptions as-is
            except ValidationError as e:
                raise HTTPException(status_code=400, detail=f"Validation error: {str(e)}")
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @app.put("/api/templates/{template_id}", response_model=TemplateResponse)
        async def update_template(template_id: str, request: UpdateTemplateRequest):
            """Update an existing template and save it to the filesystem."""
            try:
                # Check if template exists
                try:
                    current_template = self.vault.get(template_id)
                    current_spec = current_template.spec
                except TemplateNotFound:
                    raise HTTPException(status_code=404, detail=f"Template '{template_id}' not found")

                # Merge update request with current template data
                updated_version = request.version if request.version is not None else current_spec.version
                updated_description = request.description if request.description is not None else current_spec.description
                updated_template = request.template if request.template is not None else current_spec.template

                # Handle inputs merge
                updated_inputs_dict = {}
                if request.inputs is not None:
                    # Convert new input specs from dict format to InputSpec objects
                    for input_name, input_data in request.inputs.items():
                        updated_inputs_dict[input_name] = InputSpec(
                            type=input_data.get("type", "string"),
                            required=input_data.get("required", True),
                            default=input_data.get("default")
                        )
                else:
                    # Keep existing inputs
                    updated_inputs_dict = current_spec.inputs

                # Handle metadata merge
                updated_metadata = request.metadata if request.metadata is not None else current_spec.metadata

                # Create updated TemplateSpec object and validate it
                updated_spec = TemplateSpec(
                    id=current_spec.id,  # ID cannot be changed
                    version=updated_version,
                    description=updated_description,
                    template=updated_template,
                    inputs=updated_inputs_dict,
                    metadata=updated_metadata
                )

                # Save updated template to YAML file
                prompt_dir = Path(self.vault.config["prompt_dir"])
                filename = f"{updated_spec.id}.yaml"
                file_path = prompt_dir / filename

                # Create the YAML content
                yaml_content = {
                    "id": updated_spec.id,
                    "version": updated_spec.version,
                    "description": updated_spec.description,
                    "template": updated_spec.template,
                    "inputs": {
                        name: {
                            "type": input_spec.type,
                            "required": input_spec.required,
                            "default": input_spec.default
                        }
                        for name, input_spec in updated_spec.inputs.items()
                    },
                    "metadata": updated_spec.metadata
                }

                # Write to file
                with open(file_path, 'w', encoding='utf-8') as f:
                    yaml.dump(yaml_content, f, default_flow_style=False, sort_keys=False)

                # Invalidate cache to pick up the updated template
                self.vault.invalidate_cache()

                # Return the updated template
                return TemplateResponse(
                    id=updated_spec.id,
                    version=updated_spec.version,
                    description=updated_spec.description,
                    template=updated_spec.template,
                    inputs={name: {
                        "type": input_spec.type,
                        "required": input_spec.required,
                        "default": input_spec.default
                    } for name, input_spec in updated_spec.inputs.items()},
                    metadata=updated_spec.metadata
                )

            except HTTPException:
                raise  # Re-raise HTTP exceptions as-is
            except ValidationError as e:
                raise HTTPException(status_code=400, detail=f"Validation error: {str(e)}")
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @app.post("/api/templates/{template_id}/render", response_model=RenderResponse)
        async def render_template(template_id: str, request: RenderRequest):
            """Render a template with provided inputs."""
            try:
                template = self.vault.get(template_id)
                rendered = template.render(**request.inputs)

                # Get the actual inputs used (after validation and defaults)
                inputs_used = template.spec.coerce_inputs(request.inputs)

                return RenderResponse(
                    rendered=rendered,
                    inputs_used=inputs_used
                )
            except TemplateNotFound:
                raise HTTPException(status_code=404, detail=f"Template '{template_id}' not found")
            except ValidationError as e:
                raise HTTPException(status_code=400, detail=f"Validation error: {str(e)}")
            except RenderError as e:
                raise HTTPException(status_code=400, detail=f"Render error: {str(e)}")
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @app.get("/api/examples", response_model=List[TemplateResponse])
        async def get_example_templates():
            """Get example templates for the playground showcase."""
            examples = self._get_example_templates()
            return [
                TemplateResponse(
                    id=spec.id,
                    version=spec.version,
                    description=spec.description,
                    template=spec.template,
                    inputs={name: {
                        "type": input_spec.type,
                        "required": input_spec.required,
                        "default": input_spec.default
                    } for name, input_spec in spec.inputs.items()},
                    metadata=spec.metadata
                )
                for spec in examples
            ]

        @app.get("/api/health")
        async def health_check():
            """Health check endpoint."""
            try:
                template_count = len(list(self.vault.list()))
                return {
                    "status": "healthy",
                    "templates_loaded": template_count,
                    "vault_config": {
                        "prompt_dir": self.vault.config.get("prompt_dir"),
                        "logging_enabled": self.vault.config.get("logging", {}).get("enabled", False)
                    }
                }
            except Exception as e:
                raise HTTPException(status_code=503, detail=f"Unhealthy: {str(e)}")

        # Check for built React app and serve it
        playground_dir = Path(__file__).parent.parent / "playground"

        if (playground_dir / "index.html").exists():
            # Serve built React app
            app.mount("/", StaticFiles(directory=str(playground_dir), html=True), name="playground")
        else:
            # Fallback to simple HTML page
            @app.get("/", response_class=HTMLResponse)
            async def playground_ui():
                """Serve fallback UI when React app is not built."""
                return """
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Dakora Playground</title>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <style>
                        body {
                            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                            margin: 0; padding: 20px; background: #f5f5f5;
                        }
                        .container { max-width: 1200px; margin: 0 auto; }
                        .header { background: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
                        .content { background: white; padding: 20px; border-radius: 8px; }
                        .api-info { background: #e3f2fd; padding: 15px; border-radius: 4px; margin-top: 20px; }
                        .build-info { background: #fff3cd; padding: 15px; border-radius: 4px; margin-top: 20px; border: 1px solid #ffeaa7; }
                        code { background: #f5f5f5; padding: 2px 4px; border-radius: 3px; }
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div class="header">
                            <h1>🎯 Dakora Playground</h1>
                            <p>Interactive playground for prompt template development</p>
                        </div>
                        <div class="content">
                            <h2>API Endpoints</h2>
                            <ul>
                                <li><code>GET /api/templates</code> - List all templates</li>
                                <li><code>GET /api/templates/{id}</code> - Get template details</li>
                                <li><code>POST /api/templates/{id}/render</code> - Render template</li>
                                <li><code>GET /api/examples</code> - Get example templates</li>
                                <li><code>GET /api/health</code> - Health check</li>
                            </ul>

                            <div class="build-info">
                                <strong>🔧 React UI Available!</strong><br>
                                To use the full interactive playground UI, build the React app:
                                <br><br>
                                <code>cd web && npm install && npm run build</code>
                                <br><br>
                                Then restart the playground server.
                            </div>

                            <div class="api-info">
                                <strong>API Testing</strong><br>
                                Try these endpoints: <a href="/api/templates">/api/templates</a> |
                                <a href="/api/examples">/api/examples</a> |
                                <a href="/api/health">/api/health</a>
                            </div>
                        </div>
                    </div>
                </body>
                </html>
                """

        return app

    def _get_example_templates(self) -> List[TemplateSpec]:
        """Get example templates for playground showcase."""
        examples = [
            TemplateSpec(
                id="code-reviewer",
                version="1.0.0",
                description="Review code and provide feedback",
                template="""Review this code and provide feedback:

Language: {{ language }}
Code:
```{{ language }}
{{ code }}
```

Focus on:
- Code quality and best practices
- Potential bugs or issues
- Performance considerations
- Readability and maintainability

Provide specific, actionable feedback.""",
                inputs={
                    "code": {
                        "type": "string",
                        "required": True
                    },
                    "language": {
                        "type": "string",
                        "required": True,
                        "default": "python"
                    }
                },
                metadata={"category": "development", "tags": ["code-review", "programming"]}
            ),

            TemplateSpec(
                id="email-responder",
                version="1.0.0",
                description="Generate professional email responses",
                template="""Write a professional email response to this message:

Original Email:
{{ original_email }}

Response tone: {{ tone }}
{% if key_points %}
Key points to address:
{% for point in key_points %}
- {{ point }}
{% endfor %}
{% endif %}

Write a clear, {{ tone }} response that addresses the main points.""",
                inputs={
                    "original_email": {
                        "type": "string",
                        "required": True
                    },
                    "tone": {
                        "type": "string",
                        "required": False,
                        "default": "professional"
                    },
                    "key_points": {
                        "type": "array<string>",
                        "required": False
                    }
                },
                metadata={"category": "communication", "tags": ["email", "business"]}
            ),

            TemplateSpec(
                id="blog-post-generator",
                version="1.0.0",
                description="Generate blog post outlines and content",
                template="""Create a blog post about: {{ topic }}

Target audience: {{ audience }}
Tone: {{ tone }}
Length: {{ length }}

Structure:
1. Compelling headline
2. Introduction hook
3. Main content with {{ num_sections }} sections
4. Conclusion with call-to-action

{% if keywords %}
Include these keywords naturally: {{ keywords | join(", ") }}
{% endif %}

Focus on providing value and actionable insights.""",
                inputs={
                    "topic": {
                        "type": "string",
                        "required": True
                    },
                    "audience": {
                        "type": "string",
                        "required": False,
                        "default": "developers"
                    },
                    "tone": {
                        "type": "string",
                        "required": False,
                        "default": "informative"
                    },
                    "length": {
                        "type": "string",
                        "required": False,
                        "default": "medium"
                    },
                    "num_sections": {
                        "type": "number",
                        "required": False,
                        "default": 3
                    },
                    "keywords": {
                        "type": "array<string>",
                        "required": False
                    }
                },
                metadata={"category": "content", "tags": ["blog", "writing", "marketing"]}
            )
        ]

        return examples

    def run(self, debug: bool = False):
        """Start the playground server."""
        print(f"🎯 Starting Dakora Playground at http://{self.host}:{self.port}")
        print(f"📁 Prompt directory: {self.vault.config.get('prompt_dir', 'N/A')}")
        print(f"📊 Logging: {'enabled' if self.vault.logger else 'disabled'}")
        print("")

        uvicorn.run(
            self.app,
            host=self.host,
            port=self.port,
            reload=debug,
            log_level="info" if debug else "warning"
        )


def create_playground(config_path: str = None, prompt_dir: str = None,
                     host: str = "localhost", port: int = 3000) -> PlaygroundServer:
    """Create a playground server instance."""
    vault = Vault(config_path=config_path, prompt_dir=prompt_dir)
    return PlaygroundServer(vault, host=host, port=port)