from django.db import models

class DistractionBlocker(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    is_enabled = models.BooleanField(default=False)
    block_duration = models.PositiveIntegerField(help_text="Duration in minutes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {'Enabled' if self.is_enabled else 'Disabled'}"