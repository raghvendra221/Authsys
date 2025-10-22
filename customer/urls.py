from django.urls import path
from customer.views import customer_dashboard_view,password_changed_view

urlpatterns = [
    path('customer/dashboard',customer_dashboard_view,name='customer-dashboard'),
    path('password-changed/',password_changed_view,name='password-changed')
]
