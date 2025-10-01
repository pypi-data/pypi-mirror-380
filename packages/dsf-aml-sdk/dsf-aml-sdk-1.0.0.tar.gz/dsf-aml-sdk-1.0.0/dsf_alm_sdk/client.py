# ============================================
# dsf_aml_sdk/client.py
# ============================================
import requests
from typing import Dict, List, Optional, Union, Any
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

class AMLSDK:
    BASE_URL = 'https://dsf-7u1jc5aeh-jaime-alexander-jimenezs-projects.vercel.app/'
    TIERS = {'community', 'professional', 'enterprise'}
    
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
            'User-Agent': f'DSF-AML-SDK-Python/{__version__}'
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
    
    def evaluate(self, data: Dict[str, Any], config: Optional[Union[Dict, Config]] = None) -> EvaluationResult:
        """Standard evaluation"""
        if isinstance(config, Config):
            config = config.to_dict()
        if not isinstance(data, dict):
            raise ValidationError("Data must be a dictionary")
        
        request_data = {'data': data, 'config': config or {}, 'tier': self.tier}
        if self.license_key:
            request_data['license_key'] = self.license_key
        
        response = self._make_request('', request_data)
        return EvaluationResult.from_response(response)
    
    def batch_evaluate(self, data_points: List[Dict], config: Optional[Union[Dict, Config]] = None) -> List[EvaluationResult]:
        """Batch evaluation (Premium)"""
        if self.tier == 'community':
            raise LicenseError("Batch evaluation requires premium tier")
        
        if isinstance(config, Config):
            config = config.to_dict()
        
        request_data = {
            'data_batch': data_points,
            'config': config or {},
            'tier': self.tier,
            'license_key': self.license_key
        }
        
        response = self._make_request('', request_data)
        scores = response.get('scores', {})
        
        return [
            EvaluationResult(
                score=scores.get(i, 0.0),
                tier=response.get('tier'),
                confidence_level=response.get('confidence_level', 0.65),
                metrics=response.get('metrics')
            )
            for i in range(len(data_points))
        ]
    
    # ========== Knowledge Distillation Features (Premium) ==========
    
    def distill_train(self, config: Union[Dict, Config], samples: int = 1000, 
                     seed: int = 42) -> DistillationResult:
        """Train surrogate model via knowledge distillation (Premium)"""
        if self.tier == 'community':
            raise LicenseError("Distillation requires premium tier")
        
        if isinstance(config, Config):
            config = config.to_dict()
        
        request_data = {
            'action': 'translate_train',
            'config': config,
            'samples': samples,
            'seed': seed,
            'tier': self.tier,
            'license_key': self.license_key
        }
        
        response = self._make_request('', request_data)
        return DistillationResult.from_train_response(response)
    
    def distill_export(self, config: Optional[Union[Dict, Config]] = None) -> Dict:
        """Export trained surrogate model (Premium)"""
        if self.tier == 'community':
            raise LicenseError("Export requires premium tier")
        
        request_data = {
            'action': 'translate_export',
            'tier': self.tier,
            'license_key': self.license_key
        }
        
        if config:
            if isinstance(config, Config):
                config = config.to_dict()
            request_data['config'] = config
        
        return self._make_request('', request_data)
    
    def distill_predict(self, data: Dict[str, Any], config: Union[Dict, Config]) -> float:
        """Fast prediction using surrogate model (Premium)"""
        if self.tier == 'community':
            raise LicenseError("Surrogate prediction requires premium tier")
        
        if isinstance(config, Config):
            config = config.to_dict()
        
        request_data = {
            'action': 'translate_predict',
            'data': data,
            'config': config,
            'tier': self.tier,
            'license_key': self.license_key
        }
        
        response = self._make_request('', request_data)
        return response.get('score_surrogate', 0.0)
    
    def create_config(self) -> Config:
        return Config()
    
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
