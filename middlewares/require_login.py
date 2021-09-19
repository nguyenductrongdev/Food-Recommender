from flask import Blueprint, Flask, request,  jsonify, url_for, render_template, redirect, flash, send_file, session
from functools import wraps


def require_login():
    def _require_login_decorator(f):
        @wraps(f)
        def __home_decorator(*args, **kwargs):
            ND_MA = request.cookies.get("ND_MA")
            if not ND_MA:
                return redirect("/nguoi-dung/dang-nhap")
            result = f(*args, **kwargs)
            return result
        return __home_decorator
    return _require_login_decorator
