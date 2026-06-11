# InfraGuard AI

AI-powered infrastructure log analysis and incident response platform. Analyzes service logs using Google Gemini to generate severity classification, root cause analysis, SLO violation detection, and step-by-step remediation guidance.

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Framework | FastAPI |
| AI | Google Gemini API (gemini-2.0-flash-lite) |
| Server | Uvicorn |
| Containerization | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| API Docs | Swagger UI (OpenAPI 3) |

## Features

- AI-generated severity classification (CRITICAL / HIGH / MEDIUM / LOW)
- Root cause analysis from raw log input
- Affected component identification
- Step-by-step remediation guidance
- SLO violation detection with error rate calculation
- Health and metrics endpoints for observability
- Auto-generated Swagger UI documentation

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /health | Health check |
| GET | /metrics | Service metrics |
| POST | /analyze | Analyze logs with AI |
| GET | /analyze/demo | Demo with sample database crash logs |

## Getting Started

**Prerequisites:** Python 3.11+, Gemini API key from [aistudio.google.com](https://aistudio.google.com)

```bash
git clone https://github.com/sai-k21/infraguard-ai.git
cd infraguard-ai
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file:

```
GEMINI_API_KEY=your_key_here
```

Start the server:

```bash
uvicorn main:app --reload
```

Visit: `http://localhost:8000/docs`

## Example Request

```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "logs": "ERROR Database connection timeout after 30s",
    "service_name": "payment-service",
    "environment": "production"
  }'
```

## Author

**Sai Kumar Moguluri**
GitHub: [github.com/sai-k21](https://github.com/sai-k21)
