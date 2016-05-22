"""
Admin configuration to display and save UserInfo on admin panel.
"""
from django.contrib import admin

from backend.models import UserInfo


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')


admin.site.register(UserInfo, UserInfoAdmin)
