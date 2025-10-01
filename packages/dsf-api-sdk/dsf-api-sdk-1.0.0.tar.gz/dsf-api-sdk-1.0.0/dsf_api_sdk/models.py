# ============================================
# dsf_api_sdk/models.py
# ============================================
from typing import Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class Field:
    name: str
    default: Any
    weight: float = 1.0
    criticality: float = 1.5
    
    def to_dict(self) -> Dict:
        return {'default': self.default, 'weight': self.weight, 'criticality': self.criticality}

class Config:
    def __init__(self):
        self.fields: Dict[str, Field] = {}
    
    def add_field(self, name: str, default: Any, weight: float = 1.0, criticality: float = 1.5) -> 'Config':
        self.fields[name] = Field(name, default, weight, criticality)
        return self
    
    def to_dict(self) -> Dict:
        return {name: field.to_dict() for name, field in self.fields.items()}

@dataclass
class ValidationResult:
    valid: bool
    score: float
    tier: str = 'community'
    confidence_level: float = 0.65
    reason: Optional[str] = None
    metrics: Optional[Dict] = None
    
    @classmethod
    def from_response(cls, response: Dict) -> 'ValidationResult':
        return cls(
            valid=response.get('valid', False),
            score=response.get('score', 0.0),
            tier=response.get('tier', 'community'),
            confidence_level=response.get('confidence_level', 0.65),
            reason=response.get('reason'),
            metrics=response.get('metrics')
        )