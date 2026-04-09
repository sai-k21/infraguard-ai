import os
import requests
import json
from datetime import datetime

GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-lite:generateContent"

MOCK_RESPONSE = {
    "severity": "CRITICAL",
    "probable_cause": "Primary database host is unreachable due to connection pool exhaustion caused by a spike in write operations overwhelming the max_connections limit.",
    "affected_components": [
        "database-primary",
        "payment-service",
        "connection-pool",
        "write-operations"
    ],
    "remediation_steps": [
        "Immediately restart the connection pool manager to release exhausted connections",
        "Scale up database max_connections from current limit",
        "Redirect write traffic to read replica temporarily",
        "Investigate root cause of write operation spike in the last 30 minutes",
        "Set up connection pool monitoring alert at 80% threshold"
    ],
    "slo_violation": True,
    "error_rate": "94%"
}

def analyze_logs(logs: str, service_name: str, environment: str) -> dict:
    ai_provider = os.getenv("AI_PROVIDER", "mock")

    if ai_provider == "mock":
        return MOCK_RESPONSE

    api_key = os.getenv("GEMINI_API_KEY")

    prompt = f"""You are an expert SRE (Site Reliability Engineer). Analyze these infrastructure logs and respond in JSON only.

Service: {service_name}
Environment: {environment}
Logs:
{logs}

Respond with ONLY this JSON structure, no markdown:
{{
  "severity": "CRITICAL or HIGH or MEDIUM or LOW",
  "probable_cause": "one clear sentence explaining root cause",
  "affected_components": ["component1", "component2"],
  "remediation_steps": ["step 1", "step 2", "step 3"],
  "slo_violation": true or false,
  "error_rate": "percentage like 5% or 0%"
}}"""

    body = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        response = requests.post(
            f"{GEMINI_URL}?key={api_key}",
            json=body,
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        text = data["candidates"][0]["content"]["parts"][0]["text"]
        text = text.strip().replace("```json", "").replace("```", "").strip()
        return json.loads(text)
    except Exception as e:
        return {
            "severity": "UNKNOWN",
            "probable_cause": f"Analysis failed: {str(e)}",
            "affected_components": [],
            "remediation_steps": ["Check Gemini API key", "Verify network connectivity"],
            "slo_violation": False,
            "error_rate": "unknown"
        }