from django.shortcuts import render

def customer_dashboard_view(req):
    return render(req,'customer/dashboard.html')


def password_changed_view(req):
    return render(req,'customer/password_change.html')