# decors.py
# Author: Amal Alex
# Date: September 8, 2023
# Description: This decors.py demonstrates the user authorization.

import json
from flask import session
from functools import wraps

def logged_in(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if session.get("username"):
            return f(*args, **kwargs)
        else:
            return json.dumps({
                'status': 401,
                'message': 'unauthorized auth'
            })
    return decorated_func