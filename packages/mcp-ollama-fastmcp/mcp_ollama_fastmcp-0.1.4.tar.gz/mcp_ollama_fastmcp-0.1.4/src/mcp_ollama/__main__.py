"""Command-line entry point for MCP Ollama server."""

from .server import run_server

def main():
    run_server()

if __name__ == "__main__":
    main()
