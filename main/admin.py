from django.contrib import admin
from .models import DownloadStats, ContactMessage, AppVersion

@admin.register(AppVersion)
class AppVersionAdmin(admin.ModelAdmin):
    list_display = ['version', 'release_date', 'is_active', 'download_count']
    list_filter = ['is_active', 'release_date']
    search_fields = ['version', 'release_notes']
    ordering = ['-release_date']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'replied']
    list_filter = ['replied', 'created_at']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['created_at']
    ordering = ['-created_at']

@admin.register(DownloadStats)
class DownloadStatsAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'version', 'download_time']
    list_filter = ['version', 'download_time']
    search_fields = ['ip_address', 'version']
    ordering = ['-download_time']
    readonly_fields = ['ip_address', 'user_agent', 'download_time']
