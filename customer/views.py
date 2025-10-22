from django.shortcuts import render,redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import logout
# from django.contrib.auth.decorators import login_required
from core.decorators import login_and_role_required


# @login_required
@ login_and_role_required('customer')
def customer_dashboard_view(req):
    return render(req,'customer/dashboard.html')

# @login_required
@ login_and_role_required('customer')
def password_changed_view(req):
    if req.method =="POST":
        form=PasswordChangeForm(user=req.user,data=req.POST)
        if form.is_valid():
            form.save()
            logout(req)
            messages.success(req,"Password changed successfully.Please log in with the new password.")
            return redirect('login')
        # else:
            #handle form errors and display then to the user
            # for field,errors in form.errors.items():
            #     for error in errors:
            #         messages.error(req,error)
    else:
        form=PasswordChangeForm(user=req.user)
    return render(req,'customer/password_change.html',{'form':form})