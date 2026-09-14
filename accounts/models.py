from django.db import models

class GoogleUser(models.Model):
    """
    Stores core Google OAuth authentication identity data.
    Separated from personality data so core auth credentials remain immutable.
    """
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    google_sub = models.CharField(max_length=255, unique=True, db_index=True)
    profile_image = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"