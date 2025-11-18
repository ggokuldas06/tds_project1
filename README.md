Automated App Builder, Deployer & Evaluator API

This project implements a complete automated workflow for building, deploying, updating, and evaluating web applications based on instructor-provided JSON task requests. It is designed for an educational setting where students receive programmatic tasks, generate an app using an LLM, publish it, and report build metadata for automated assessment.

-> Overview

The API accepts structured POST requests describing a task (brief, checks, attachments, and metadata).
For each request, the system:

Validates the secret provided in the task request.

Generates an application using LLM assistance based on the task brief.

Creates a GitHub repository, adds required files (e.g., MIT license, README), and deploys via GitHub Pages.

Reports build metadata (repo URL, commit SHA, pages URL) back to the provided evaluation endpoint.

Handles Round 2 revision tasks, updates the existing repo, and re-deploys.

This supports a complete build–evaluate–revise loop required by the instructors’ automation scripts.

🔗 API Endpoint

Your deployment is available at:

https://tds-project1-c0n2.onrender.com

The API accepts JSON POST requests:

curl -X POST https://tds-project1-c0n2.onrender.com \
  -H "Content-Type: application/json" \
  -d '{"brief": "...", "secret": "...", ...}'


The server returns a JSON 200 response on success.

-> Features

Secret-validated task processing

Attachment parsing (data URIs)

LLM-assisted code generation

GitHub repo creation & configuration

Automatic MIT license insertion

GitHub Pages deployment & verification

Evaluation metadata callback with retry logic

Round-based updates (round 1 → round 2)

📁 Repository Output

Each generated repository includes:

index.html and supporting code for the requested app

LICENSE (MIT)

Professional README.md describing the generated project

Clean commit history with no leaked secrets

Public GitHub Pages deployment

-> Evaluation Callback Format

The API reports results back using:

{
  "email": "...",
  "task": "...",
  "round": 1,
  "nonce": "...",
  "repo_url": "...",
  "commit_sha": "...",
  "pages_url": "..."
}


Returned to: evaluation_url provided in the task.

