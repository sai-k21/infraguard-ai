# InfraGuard AI

AI-powered infrastructure log analysis and incident response platform that analyzes service logs using Google Gemini to generate severity classification, root cause analysis, SLO violation detection, and step-by-step remediation guidance.

## Features

- AI-generated severity classification (CRITICAL/HIGH/MEDIUM/LOW)
- Probable root cause analysis from raw logs
- Affected component identification
- Step-by-step remediation guidance
- SLO violation detection
- Error rate calculation
- /health and /metrics endpoints for observability
- Swagger/OpenAPI 3 documentation (FastAPI auto-generated)
- Docker + docker-compose support
- GitHub Actions CI/CD pipeline

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Framework | FastAPI |
| AI | Google Gemini API (gemini-2.0-flash-lite) |
| Server | Uvicorn |
| Containerization | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| API Docs | Swagger UI (auto-generated) |

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /health | Health check |
| GET | /metrics | Service metrics |
| POST | /analyze | Analyze logs with AI |
| GET | /analyze/demo | Demo with sample database crash logs |

## Running Locally

### Prerequisites

- Python 3.11+
- Gemini API key from aistudio.google.com

### Setup

Clone and install:

    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt

Create a .env file:

    GEMINI_API_KEY=your_key_here

Start the server:

    uvicorn main:app --reload

Visit: http://localhost:8000/docs

## Example Request

    curl -X POST http://localhost:8000/analyze
      -H "Content-Type: application/json"
      -d '{"logs": "ERROR Database connection timeout", "service_name": "payment-service", "environment": "production"}'

## Author

**Sai Kumar Moguluri**

- LinkedIn: https://linkedin.com/in/sai-1899k
- GitHub: https://github.com/sai-k21
