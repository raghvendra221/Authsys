from django.shortcuts import render,redirect
from account.forms import RegistrationForm,LoginForm,PasswordResetForm,SetNewPasswordForm
from django.contrib.auth import logout
from django.contrib import messages
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
            messages.success(
                req,
                'Registration successful! Please check your email to activate your account',
                )
            return redirect('login')
    else:
        form=RegistrationForm()
    return render(req,'account/register.html',{'form':form})

def login(req):
    if req.method == "POST":
        form =LoginForm(req.POST)
        if form.is_valid():
            return redirect('customer-dashboard')
    else:
        form=LoginForm()
    return render(req,'account/login.html',{'form':form})


def password_reset(req):
    if req.method == "POST":
        form =PasswordResetForm(req.POST)
        if form.is_valid():
            pass
            # return redirect('customer_dashboard')
    else:
        form=PasswordResetForm()
    return render(req,'account/pass_reset.html',{'form':form})



def password_reset_confirm(request):
    if request.method == "POST":
        form = SetNewPasswordForm(request.POST)
        if form.is_valid():
            # Here you would normally set the user's new password
            return redirect('password_reset_complete')  # redirect to a success page
    else:
        form = SetNewPasswordForm()
    
    return render(request, 'account/pass_reset_confirmation.html', {'form': form})

    
def logout_view(request):
    logout(request)  # Ends the session
    return redirect('home')
