from django.urls import path
from account.views import home,register,login,password_reset,password_reset_confirm,logout_view

urlpatterns = [
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('password_reset/',password_reset,name='password-reset'),
    path('password_reset_confirm/<uidb64>/<token>/',password_reset_confirm,name='password-reset-confirm'),
    path('logout/', logout_view, name='logout')
]