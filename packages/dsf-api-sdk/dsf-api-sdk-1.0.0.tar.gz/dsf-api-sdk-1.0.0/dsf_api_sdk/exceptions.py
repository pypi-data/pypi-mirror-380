# ============================================
# dsf_api_sdk/exceptions.py
# ============================================
class APISDKError(Exception):
    pass

class ValidationError(APISDKError):
    pass

class LicenseError(APISDKError):
    pass

class APIError(APISDKError):
    def __init__(self, message: str, status_code: Optional[int] = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


