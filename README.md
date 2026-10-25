# Linux Survival Guide

A personal learning project: a small collection of Linux, Bash, and VPS notes, plus a basic Python HTTP-server experiment.

## Repository contents
- .github/workflows/ci.yml — Python compile check
- app.py — standard-library HTTP server experiment
- mysite/ — standalone HTML/CSS pages
- README.md — project notes

## Python HTTP experiment
app.py uses Python's standard library (http.server) and listens on 127.0.0.1:3000.

Current endpoints:
- GET /hello — returns a simple greeting.
- POST /contact — accepts URL-encoded name, email, and message fields and appends them to messages.txt.

The server is a learning prototype. It is not a production web application: it uses the basic HTTPServer, has no TLS or authentication, and the contact handler writes submitted values to a local file. Do not expose it directly to the public internet or submit real personal data.

The mysite/ directory contains standalone HTML/CSS pages. The current Python server does not serve those pages; use a static web server such as Nginx to host them.

## Run the endpoint experiment
Start it with: python3 app.py
Test from another terminal: curl http://127.0.0.1:3000/hello

The application currently uses only Python's standard library, so no third-party dependency installation is needed.

## Checks
GitHub Actions runs Python bytecode compilation on pushes and pull requests. The equivalent local command is: python -m compileall -q .

## Learning goals
- Linux and VPS fundamentals
- Bash and command-line practice
- Python HTTP handling
- Nginx and static-site deployment concepts
- Git and GitHub workflow

This repository is a work in progress. Documentation describes the current implementation; planned features are not presented as already completed.