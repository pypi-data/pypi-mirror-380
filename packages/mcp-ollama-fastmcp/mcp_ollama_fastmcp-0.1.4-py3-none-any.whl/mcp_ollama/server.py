#!/usr/bin/env python

"""MCP server implementation for Ollama integration."""

from mcp.server.fastmcp import FastMCP
from ollama import Client


import os
DEFAULT_URL = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")

ollama = Client(host=DEFAULT_URL)

# Initialize FastMCP server
mcp = FastMCP(
    "ollama",
    dependencies=["ollama"]
)

@mcp.tool()
async def list_models() -> str:
    """List all downloaded Ollama models"""
    try:
        models = ollama.list()
        if not models.get('models'):
            return "No models found"

        formatted_models = []
        for model in models['models']:
            formatted_models.append(
                f"Name: {model.get('model', 'Unknown')}\n"
                f"Size: {model.get('size', 'Unknown')}\n"
                f"Modified: {model.get('modified_at', 'Unknown')}\n"
                "---"
            )
        return "\n".join(formatted_models)
    except Exception as e:
        return f"Error listing models: {str(e)}"

@mcp.tool()
async def show_model(name: str) -> str:
    """Get detailed information about a specific model

    Args:
        name: Name of the model to show information about
    """
    try:
        model_info = ollama.show(name)
        if not model_info:
            return f"No information found for model {name}"

        # Format the model information
        details = [
            f"Model: {name}",
            f"License: {model_info.get('license', 'Unknown')}",
            f"Format: {model_info.get('format', 'Unknown')}",
            f"Parameter Size: {model_info.get('parameter_size', 'Unknown')}",
            f"Quantization Level: {model_info.get('quantization_level', 'Unknown')}"
        ]

        # Add system prompt if available
        if model_info.get('system'):
            details.append(f"\nSystem Prompt:\n{model_info['system']}")

        # Add template if available
        if model_info.get('template'):
            details.append(f"\nTemplate:\n{model_info['template']}")

        return "\n".join(details)
    except Exception as e:
        return f"Error getting model information: {str(e)}"

@mcp.tool()
async def ask_model(model: str, question: str) -> str:
    """Ask a question to a specific Ollama model

    Args:
        model: Name of the model to use (e.g., 'llama2')
        question: The question to ask the model
    """
    try:
        response = ollama.chat(
            model=model,
            messages=[{
                'role': 'user',
                'content': question
            }]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error querying model: {str(e)}"

def run_server() -> None:
    """Run the MCP server using stdio transport."""
    mcp.run(transport='stdio')

if __name__ == "__main__":
    run_server()
