#creating decorator for restric view, so that even after the login seller cannot access the customer dashboard and vise versa

from django.contrib.auth.decorators import login_required
from functools import wraps
from django.http import HttpResponseForbidden


error_403_html="""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Access Forbidden</title>
<style>
    body {
        margin: 0;
        padding: 0;
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #f0f0f0, #e0e0e0);
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .container {
        background: rgba(255, 255, 255, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 20px;
        backdrop-filter: blur(12px) saturate(180%);
        -webkit-backdrop-filter: blur(12px) saturate(180%);
        box-shadow: 0 12px 40px rgba(0,0,0,0.15);
        padding: 60px 50px;
        text-align: center;
        max-width: 500px;
    }

    /* ---------- Single-line header ---------- */
    .header-line {
        font-size: 36px;
        font-weight: 700;
        color: #dc3545;
        margin-bottom: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px; /* space between elements */
    }

    .header-line span {
        display: inline-block;
    }

    /* Dash separator */
    .separator {
        color: #555555;
        font-weight: 600;
    }

    /* ---------- Message ---------- */
    p {
        font-size: 16px;
        color: #333333;
        margin-bottom: 30px;
        line-height: 1.5;
    }

    /* ---------- Button ---------- */
    a.button {
        display: inline-block;
        background: linear-gradient(90deg, #3b82f6, #60a5fa);
        color: #ffffff;
        padding: 14px 32px;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.3s ease;
    }

    a.button:hover {
        background: linear-gradient(90deg, #2563eb, #3b82f6);
        transform: translateY(-2px);
    }

    @media (max-width: 480px) {
        .container {
            padding: 40px 25px;
        }
        .header-line {
            font-size: 28px;
            gap: 5px;
        }
        p {
            font-size: 14px;
        }
        a.button {
            padding: 12px 24px;
            font-size: 14px;
        }
    }
</style>
</head>
<body>
    <div class="container">
        <div class="header-line">
            
            
            <span>403</span>
            <span class="separator">—</span>
            <span>Access Forbidden</span>
        </div>
        <p>Sorry! You don’t have permission to access this page.<br>
           Please contact support or return to the home page.</p>
        <a href="/" class="button">Return to Home</a>
    </div>
</body>
</html>

"""

def login_and_role_required(required_role):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(req,*args,**kwargs):
            user=req.user
            if required_role=="customer" and not user.is_customer:
                return HttpResponseForbidden(error_403_html)
            if required_role=="seller" and not user.is_seller:
                return HttpResponseForbidden(error_403_html)       
            return view_func(req,*args,**kwargs)
        return _wrapped_view
    return decorator     


 