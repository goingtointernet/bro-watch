from django.contrib import admin
from .models import User

# Register User
@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id','username','first_name','last_name','email']
