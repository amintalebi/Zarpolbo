from django.contrib import admin

# Register your models here.
from account.models import UserInfo


admin.site.register(UserInfo)
