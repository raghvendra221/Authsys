from account.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

class UserModelAdmin(UserAdmin):
    model =User
    list_display=["id","email","name","is_active","is_superuser","is_staff","is_customer","is_seller"]
    list_filter =["is_superuser"]
    fieldsets =[
        ("User Credentials",{"fields":["email","password"]}),
        ("Personal Information",{"fields":["name"]}),
        ("permissions",{"fields":["is_staff","is_superuser","is_cutomer","is_seller"]}),
    ]

    add_fieldsets=[
        (
    {
        "classes":["wide"],
        "fields":["email","password","password2"],

    },
        ),
    ]

    search_fields=["email"]
    ordering=["email","id"]
    filter_horizontal=[]

admin.site.register(User,UserModelAdmin)
