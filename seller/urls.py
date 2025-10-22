from django.urls import path
from seller.views import seller_dashboard

urlpatterns = [
    path('seller/dashboard',seller_dashboard,name='seller-dashboard'),
]