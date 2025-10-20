from django.urls import path
from seller.views import seller_dashboard

urlpatterns = [
    path('dashboard',seller_dashboard,name='seller-dashboard'),
]