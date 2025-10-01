# ============================================
# dsf_api_sdk/client.py
# ============================================
import requests
from typing import Dict, Optional, Union, Any
from urllib.parse import urljoin
import time
from functools import wraps
import logging

logger = logging.getLogger(__name__)

def retry_on_failure(max_retries: int = 3, delay: float = 1.0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (requests.RequestException, APIError) as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        time.sleep(delay * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator

class APISDK:
    BASE_URL = 'https://dsf-gv7x85cv0-jaime-alexander-jimenezs-projects.vercel.app/'
    TIERS = {'community', 'professional', 'enterprise'}
    
    # Default validation config for API requests
    DEFAULT_API_CONFIG = {
        'auth_token_present': {'default': True, 'weight': 5.0, 'criticality': 5.0},
        'auth_token_valid_length': {'default': True, 'weight': 5.0, 'criticality': 5.0},
        'user_verified': {'default': True, 'weight': 5.0, 'criticality': 5.0},
        'requests_per_minute': {'default': 30, 'weight': 4.0, 'criticality': 4.0},
        'token_age_minutes': {'default': 15, 'weight': 4.0, 'criticality': 3.5},
        'ip_reputation_score': {'default': 75, 'weight': 4.0, 'criticality': 3.0},
    }
    
    def __init__(self, license_key: Optional[str] = None, tier: str = 'community',
                 base_url: Optional[str] = None, timeout: int = 30, verify_ssl: bool = True):
        if tier not in self.TIERS:
            raise ValidationError(f"Invalid tier: {self.TIERS}")
        
        self.license_key = license_key
        self.tier = tier
        self.base_url = base_url or self.BASE_URL
        self.timeout = timeout
        self.verify_ssl = verify_ssl
        
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': f'DSF-API-SDK-Python/{__version__}'
        })
        
        if tier != 'community' and license_key:
            self._validate_license()
    
    def _validate_license(self):
        try:
            response = self._make_request('', {
                'data': {}, 'config': {'test': {'default': 1, 'weight': 1.0}},
                'tier': self.tier, 'license_key': self.license_key
            })
            if not response.get('tier'):
                raise LicenseError("License validation failed")
        except APIError as e:
            if e.status_code == 403:
                raise LicenseError(f"Invalid license: {e.message}")
            raise
    
    @retry_on_failure(max_retries=3)
    def _make_request(self, endpoint: str, data: Dict) -> Dict:
        url = urljoin(self.base_url, endpoint)
        try:
            response = self.session.post(url, json=data, timeout=self.timeout, verify=self.verify_ssl)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 403:
                raise LicenseError(response.json().get('error', 'License error'))
            elif response.status_code >= 400:
                raise APIError(response.json().get('error', 'API error'), status_code=response.status_code)
        except requests.RequestException as e:
            raise APIError(f"Request failed: {str(e)}")
    
    def validate_request(self, request_data: Dict[str, Any], 
                        config: Optional[Union[Dict, Config]] = None) -> ValidationResult:
        """Validate an API request"""
        if isinstance(config, Config):
            config = config.to_dict()
        if not isinstance(request_data, dict):
            raise ValidationError("Request data must be a dictionary")
        
        # Use default config if none provided
        final_config = config or self.DEFAULT_API_CONFIG
        
        request_payload = {
            'data': request_data,
            'config': final_config,
            'tier': self.tier
        }
        if self.license_key:
            request_payload['license_key'] = self.license_key
        
        response = self._make_request('', request_payload)
        return ValidationResult.from_response(response)
    
    def create_config(self) -> Config:
        """Create custom validation config"""
        return Config()
    
    def get_default_config(self) -> Dict:
        """Get default API validation config"""
        return self.DEFAULT_API_CONFIG.copy()
    
    def get_metrics(self) -> Optional[Dict]:
        if self.tier == 'community':
            return None
        response = self._make_request('', {
            'data': {}, 'config': {}, 'tier': self.tier, 'license_key': self.license_key
        })
        return response.get('metrics')
    
    def close(self):
        self.session.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()