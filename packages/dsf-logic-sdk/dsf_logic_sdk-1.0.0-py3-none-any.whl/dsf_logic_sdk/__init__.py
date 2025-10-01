# ============================================
# dsf_logic_sdk/__init__.py
# ============================================
"""DSF Logic SDK - Conditional Logic Evaluation"""

__version__ = '1.0.0'
__author__ = 'Jaime Alexander Jimenez'
__email__ = 'contacto@softwarefinanzas.com.co'

from .client import LogicSDK
from .exceptions import LogicSDKError, ValidationError, LicenseError, APIError
from .models import Field, Config, EvaluationResult

__all__ = [
    'LogicSDK',
    'Field',
    'Config',
    'EvaluationResult',
    'LogicSDKError',
    'ValidationError',
    'LicenseError',
    'APIError'
]