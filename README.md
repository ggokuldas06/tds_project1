# Automated App Builder, Deployer & Evaluator API

This project implements an automated pipeline that receives instructor-generated tasks, builds a corresponding web application using LLM assistance, deploys it to GitHub Pages, and reports metadata back to an evaluation service.

It supports multi-round workflows (Build → Evaluate → Revise).

## 🔗 Live API Endpoint

**https://tds-project1-c0n2.onrender.com**

---

## 🚀 Project Overview

The API receives a JSON task request containing:

- **brief** – description of the app to generate
- **attachments** – data-URI files to include
- **checks** – evaluation criteria
- **secret** – student-provided authentication token
- **task / round / nonce** – identifiers for tracking
- **evaluation_url** – where to send build metadata

Upon receiving the request, the system:

1. **Validates the secret**
2. **Generates the app** using LLM-driven code creation
3. **Creates a public GitHub repository**
4. **Adds an MIT License and README**
5. **Deploys the project using GitHub Pages**
6. **Reports repo and deployment details** back to the evaluation URL
7. For Round 2, **updates the existing repo** and redeploys

---

## 📡 API Usage

Send a POST request:

```bash
curl -X POST https://tds-project1-c0n2.onrender.com \
  -H "Content-Type: application/json" \
  -d '{"brief": "...", "secret": "...", "task": "...", "round": 1}'
```

A `200 OK` JSON response is returned upon successful processing.

---

## 🛠 Core Features

- Secret-protected request handling
- Data-URI attachment parsing
- LLM-generated application scaffolding
- Automated GitHub repository creation
- MIT License insertion
- GitHub Pages deployment with status verification
- Evaluation callback with exponential retry
- Round-based revision and redeployment workflow

---

## 📁 Repository Output Structure

Each generated repo includes:

```
/LICENSE            # MIT License
/README.md          # Professional documentation
/index.html         # App entry point
/assets/...         # Any generated or attachment-based assets
```

GitHub Pages is enabled for every build.

---

## 📤 Evaluation Callback Format

Once deployed, the API sends:

```json
{
  "email": "...",
  "task": "...",
  "round": 1,
  "nonce": "...",
  "repo_url": "https://github.com/user/repo",
  "commit_sha": "abc123",
  "pages_url": "https://user.github.io/repo/"
}
```

This is POSTed to the provided `evaluation_url`.

---

