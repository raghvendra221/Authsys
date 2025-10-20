from account.models import User
from django.contrib import admin

@admin.register(User)
class profilemodeladmin(admin.ModelAdmin):
    list_display =['name','email','password']