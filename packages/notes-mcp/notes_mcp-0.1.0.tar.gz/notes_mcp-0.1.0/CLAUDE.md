# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Model Context Protocol (MCP) server that provides tools for managing markdown notes with YAML frontmatter. The server is built using FastMCP and provides file operations specifically designed for structured markdown documents.

## Architecture

**Single File Architecture**: The entire server implementation is contained in `server.py`. This is a FastMCP-based server that exposes tools for note management.

**Key Components**:
- **FastMCP Server**: Main server instance that handles MCP protocol communication
- **Root Directory Management**: All operations are scoped to a configurable root directory passed as a command line argument
- **YAML Frontmatter Validation**: The `write` function validates YAML frontmatter format and syntax
- **File Operations**: Standard file/directory operations (read, write, glob, mkdir, rm, rmdir) scoped to the notes directory
- **Search Functionality**: Full-text search across YAML frontmatter and optionally markdown content

## Development Commands

**Running the Server**:
```bash
python server.py <root_directory>
```

**Dependency Management**:
```bash
uv sync  # Install dependencies
```

## Key Implementation Details

**File Structure**: All notes must be markdown files (`.md`) with YAML frontmatter in the format:
```
---
key: value
---
markdown content
```

**Search Implementation**: The `search` function operates on `.md` files only and performs case-insensitive matching. It can search in YAML frontmatter by default, with optional markdown content search via the `in_markdown` parameter.

**Path Handling**: All file operations are relative to the configured root directory. The server uses Python's `pathlib.Path` for safe path manipulation.

**Error Handling**: YAML frontmatter validation throws `ValueError` for malformed frontmatter. File operations use built-in Python file handling with appropriate error propagation.