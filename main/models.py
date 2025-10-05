from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property

class DownloadStats(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    download_time = models.DateTimeField(default=timezone.now)
    version = models.CharField(max_length=20, default='1.0')
    
    class Meta:
        verbose_name_plural = "Download Statistics"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    replied = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']

class AppVersion(models.Model):
    version = models.CharField(max_length=20)
    apk_file = models.FileField(upload_to='downloads/')
    release_notes = models.TextField()
    release_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    download_count = models.PositiveIntegerField(default=0)

    @cached_property
    def file_size_mb(self):
        if self.apk_file and hasattr(self.apk_file, 'size'):
            size_mb = self.apk_file.size / (1024 * 1024)
            return f"{size_mb:.1f} MB"
        return "N/A"
    
    class Meta:
        ordering = ['-release_date']
