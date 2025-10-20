from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser


#custome user creation
class UserManager(BaseUserManager):
    def create_user(self,email,password=None):
        #create and save an User with given email and password
        if not email:
            raise ValueError("user must have an valid email")
        user =self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True.')

        #create and saves a superuser with the given email and password.
        user =self.create_user(email,password)
        user.is_staff=True
        user.is_superuser=True
        user.is_customer=True
        user.is_seller=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email =models.EmailField(max_length=225,unique=True)
    name = models.CharField(max_length=200)
    city =models.CharField(max_length=225)
    is_active=models.BooleanField(default=False)
    is_staff= models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    is_customer= models.BooleanField(default=True)
    is_seller= models.BooleanField(default=False)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    USERNAME_FIELD='email'
    objects =UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_superuser
    
    def has_module_perms(self,app_label):
        return self.is_superuser

