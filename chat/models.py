from django.db import models
from accounts.models import GoogleUser


# --- Neon table placeholders   not migrated, not active yet ---
#
# Right now chat history lives in request.session only (see chat/views.py).
# These are commented out so the schema shape is decided in advance.

# class ChatMessage(models.Model):
#     ...

# class MemoryEmbedding(models.Model):
#     ...


class UserPersonality(models.Model):
    """
    Stores evolving user personality preferences, quick-setup fields,
    flexible psychological answers, and the final derived personality summary.
    Linked 1-to-1 to GoogleUser.
    """
    user = models.OneToOneField(GoogleUser, on_delete=models.CASCADE, related_name="personality")

    # Quick setup fields (Page 2 of signup)
    tone_preference = models.CharField(max_length=50, default="Warm")
    communication_style = models.CharField(max_length=255, blank=True, null=True)
    scenario_response = models.CharField(max_length=255, blank=True, null=True)
    boundaries = models.CharField(max_length=255, blank=True, null=True)

    # Flexible field for future deeper ~5 psychological questions
    psychological_answers = models.JSONField(default=dict, blank=True)

    # The final derived text paragraph that eventually feeds into genai.py's personality_context
    personality_summary = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Personality Profile for {self.user.name} [Tone: {self.tone_preference}]"