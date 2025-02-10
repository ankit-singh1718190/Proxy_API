from django.contrib import admin
from .models import ResidentialIP, ProxyUsage

@admin.register(ResidentialIP)
class ResidentialIPAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'is_active', 'created_at')

@admin.register(ProxyUsage)
class ProxyUsageAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'usage_start', 'usage_end', 'data_transferred')