import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from datetime import datetime
from app.models.models import LogAnalysisRequest, IncidentReport, ApiResponse
from app.services.gemini_service import analyze_logs

load_dotenv()

app = FastAPI(
    title="InfraGuard AI",
    description="AI-powered infrastructure log analysis and incident response platform using Google Gemini",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/health", tags=["System"])
def health():
    return ApiResponse(
        success=True,
        message="InfraGuard AI is running",
        data={"status": "healthy", "version": "1.0.0"},
        timestamp=datetime.now().isoformat()
    )

@app.get("/metrics", tags=["System"])
def metrics():
    return ApiResponse(
        success=True,
        message="Metrics retrieved",
        data={
            "service": "infraguard-ai",
            "uptime": "running",
            "ai_model": "gemini-2.0-flash-lite",
            "endpoints": ["/health", "/metrics", "/analyze", "/analyze/demo"]
        },
        timestamp=datetime.now().isoformat()
    )

@app.post("/analyze", tags=["Analysis"])
def analyze(request: LogAnalysisRequest):
    result = analyze_logs(
        logs=request.logs,
        service_name=request.service_name,
        environment=request.environment
    )
    report = IncidentReport(
        service_name=request.service_name,
        environment=request.environment,
        severity=result.get("severity", "UNKNOWN"),
        probable_cause=result.get("probable_cause", "Unknown"),
        affected_components=result.get("affected_components", []),
        remediation_steps=result.get("remediation_steps", []),
        slo_violation=result.get("slo_violation", False),
        error_rate=result.get("error_rate", "unknown"),
        analyzed_at=datetime.now().isoformat()
    )
    return ApiResponse(
        success=True,
        message="Log analysis completed",
        data=report.model_dump(),
        timestamp=datetime.now().isoformat()
    )

@app.get("/analyze/demo", tags=["Analysis"])
def analyze_demo():
    demo_logs = """
2026-04-08 19:00:01 ERROR Database connection timeout after 30s - retry 1/3
2026-04-08 19:00:05 ERROR Database connection timeout after 30s - retry 2/3
2026-04-08 19:00:09 ERROR Database connection timeout after 30s - retry 3/3
2026-04-08 19:00:10 CRITICAL Failed to connect to primary database host db-primary:5432
2026-04-08 19:00:10 ERROR 47 requests failed - connection pool exhausted
2026-04-08 19:00:11 WARN Falling back to read replica db-replica:5432
2026-04-08 19:00:12 ERROR Write operations failing - replica is read-only
2026-04-08 19:00:15 CRITICAL SLO breach detected - error rate 94% exceeds threshold 1%
"""
    result = analyze_logs(
        logs=demo_logs,
        service_name="payment-service",
        environment="production"
    )
    report = IncidentReport(
        service_name="payment-service",
        environment="production",
        severity=result.get("severity", "UNKNOWN"),
        probable_cause=result.get("probable_cause", "Unknown"),
        affected_components=result.get("affected_components", []),
        remediation_steps=result.get("remediation_steps", []),
        slo_violation=result.get("slo_violation", False),
        error_rate=result.get("error_rate", "unknown"),
        analyzed_at=datetime.now().isoformat()
    )
    return ApiResponse(
        success=True,
        message="Demo analysis completed",
        data=report.model_dump(),
        timestamp=datetime.now().isoformat()
    )