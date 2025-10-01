# ============================================
# dsf_logic_sdk/exceptions.py
# ============================================
class LogicSDKError(Exception):
    pass

class ValidationError(LogicSDKError):
    pass

class LicenseError(LogicSDKError):
    pass

class APIError(LogicSDKError):
    def __init__(self, message: str, status_code: Optional[int] = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code