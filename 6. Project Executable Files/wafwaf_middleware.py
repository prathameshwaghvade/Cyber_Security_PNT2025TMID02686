# waf/waf_middleware.py
from functools import wraps
from flask import request

def waf_check(f):
    """WAF that checks for common attack vectors like SQL injection, XSS."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Block known attack patterns
        dangerous_patterns = ["' OR 1=1 --", "<script>", "<img src=", "DROP TABLE"]
        user_input = request.data.decode('utf-8')
        
        for pattern in dangerous_patterns:
            if pattern.lower() in user_input.lower():
                return "Suspicious activity detected! Request blocked.", 403
        return f(*args, **kwargs)
    
    return decorated_function
