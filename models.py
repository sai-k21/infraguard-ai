from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class LogAnalysisRequest(BaseModel):
    logs: str
    service_name: Optional[str] = "unknown-service"
    environment: Optional[str] = "production"

class IncidentReport(BaseModel):
    service_name: str
    environment: str
    severity: str
    probable_cause: str
    affected_components: List[str]
    remediation_steps: List[str]
    slo_violation: bool
    error_rate: str
    analyzed_at: str

class ApiResponse(BaseModel):
    success: bool
    message: str
    data: Optional[dict] = None
    timestamp: str