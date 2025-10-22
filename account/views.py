from django.shortcuts import render,redirect
from account.forms import RegistrationForm,LoginForm,PasswordResetForm
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import logout,authenticate,login as auth_login
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
from account.utils import send_activation_email,send_reset_password_email
from account.models import User
from django.contrib.auth.forms import SetPasswordForm
def home(req):
    return render(req,'account/home.html')

def register(req):
    if req.method == "POST":
        form =RegistrationForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])#this will save the pasword as hash intead of raw password(mtlb code language mai save hoga )
            user.is_active=False
            user.save()

            uidb64=urlsafe_base64_encode(force_bytes(user.pk))
            token= default_token_generator.make_token(user)
            activation_link=reverse(
                'activate',kwargs={'uidb64':uidb64,'token':token}
            )
            activation_url=f'{settings.SITE_DOMAIN}{activation_link}'
            send_activation_email(user,activation_url)

            messages.success(
                req,
                'Registration successful! Please check your email to activate your account',
                )
            return redirect('login')
    else:
        form=RegistrationForm()
    return render(req,'account/register.html',{'form':form})


def activate_account(req,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)

        if user.is_active:
            messages.warning(req,"This account has already been activate")

            return redirect('login')
        
        if default_token_generator.check_token(user,token):
            user.is_active=True
            user.save()
            messages.success(
                req,"Your account has been activated succesfully!!"
            )
            return redirect('login')
        else:
            messages.error(req,"The activation link is invalid or has expired.")


    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        messages.error(req,"Invalid activation link.")
        return redirect('login')

def login(req):
    #first check user authentication
    if req.user.is_authenticated:
        #check is user is seller
        if req.user.is_seller:
            return redirect('seller-dashboard')
        elif req.user.is_customer:
            return redirect('customer-dashboard')
        return redirect('home')
    

    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
        
            try:
                user=User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(req,"Invalid email or password.")
                return redirect('login')
        
            if not user.is_active:
                messages.error(
                req,'Your account is inactive.Please activate your account'
            )
                return redirect('login')
        
        #authentication work
            user=authenticate(req,email=email,password=password)

            if user is not None:
                auth_login(req,user)
                if req.user.is_seller:
                    return redirect('seller-dashboard')
                elif req.user.is_customer:
                    return redirect('customer-dashboard')
                else:
                    messages.error(
                    req,"You do not have permission to access this area."
                )
                    return redirect('home')
            
            else:
                messages.error(req,"Invalid email or password.")
                return redirect('login')
        else:
            return render(req,'account/login.html',{'form':form})
    else:
        form=LoginForm()
    return render(req,'account/login.html',{'form':form})


def password_reset(req):
    if req.method == "POST":
        form =PasswordResetForm(req.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            user =User.objects.filter(email=email).first()
            if user:
                uidb64=urlsafe_base64_encode(force_bytes(user.pk))
                token= default_token_generator.make_token(user)
                reset_url=reverse(
                'password-reset-confirm',kwargs={'uidb64':uidb64,'token':token}
            )
            absolute_reset_url=f"{req.build_absolute_uri(reset_url)}"
            send_reset_password_email(user,absolute_reset_url)
            messages.success(req,'We have sent you a password rest link.Please check your email.')

            return redirect('login')
    else:
        form=PasswordResetForm()
    return render(req,'account/pass_reset.html',{'form':form})



def password_reset_confirm(req,uidb64,token):
    try:
        uid =force_str(urlsafe_base64_decode(uidb64))
        user =User.objects.get(pk=uid)
        if not default_token_generator.check_token(user,token):
            messages.error(req,('This link has expired or is invalid'))
            return redirect('password-reset')
        if req.method == "POST":
            form = SetPasswordForm(user,req.POST)
            if form.is_valid():
                form.save()
            # Here you would normally set the user's new password
                messages.success(req,'Your password has been successfully reser')
                return redirect('login')  # redirect to a success page
            
        else:
            form = SetPasswordForm(user)
        return render(req,'account/pass_reset_confirmation.html',{'form':form,'uidb64':uidb64,'token':token})
    

    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        messages.error(req,'An error ocuured.Please try again later.')
        return redirect('password-reset')
            
    
   
    
def logout_view(request):
    logout(request)  # Ends the session
    return redirect('home')
