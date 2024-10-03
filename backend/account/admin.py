from django.contrib import admin
from .models import AppAccount

@admin.register(AppAccount)
class AppAccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_staff', 'is_active')
    search_fields = ('email', 'username')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
