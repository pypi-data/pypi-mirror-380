# ============================================
# dsf_access_sdk/exceptions.py
# ============================================
class AccessSDKError(Exception):
    pass

class ValidationError(AccessSDKError):
    pass

class LicenseError(AccessSDKError):
    pass

class APIError(AccessSDKError):
    def __init__(self, message: str, status_code: Optional[int] = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code