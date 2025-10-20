from django.shortcuts import render

def seller_dashboard(req):
    return render(req,'seller/dashboard.html')