from django import forms
from account.models import User

class RegistrationForm(forms.ModelForm):
    #role based registration(as a seller or customer)
    ROLE_CHOICES = (
    ('', 'Select your role'),   # default empty option
    ('customer','Customer'),
    ('seller','Seller')
)

    role = forms.ChoiceField(
    choices=ROLE_CHOICES,
    widget=forms.Select(attrs={
        'class': 'form-control glassy-input', 
    }),
    required=True
)


    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
         label="Password"
        )
    
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
         label="Confirm Password"
        )

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'confirm_password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
               
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already registered.")
        return email

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

class PasswordResetForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your registered email'
        }),
        label="Email"
    )
    def clean_email(self):
        email=self.cleaned_data.get('email')
        #check if a user with this exail exist
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('' \
            'No account is associated with this email')
        return email



# class SetNewPasswordForm(forms.Form):
#     new_password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'}),
#         label="New Password"
#     )
#     confirm_password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
#         label="Confirm Password"
#     )

#     def clean(self):
#         cleaned_data = super().clean()
#         password1 = cleaned_data.get("new_password")
#         password2 = cleaned_data.get("confirm_password")

#         if password1 != password2:
#             raise forms.ValidationError("Passwords do not match.")
#         return cleaned_data
