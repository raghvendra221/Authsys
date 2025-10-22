from django.urls import path
from account.views import home,register,login,password_reset,password_reset_confirm,logout_view,activate_account

urlpatterns = [
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('activate/<str:uidb64>/<str:token>/',activate_account,name='activate'),
    path('login/',login,name='login'),
    path('password_reset/',password_reset,name='password-reset'),
    path('password_reset_confirm/<str:uidb64>/<str:token>/',password_reset_confirm,name='password-reset-confirm'),
    path('logout/', logout_view, name='logout')
]