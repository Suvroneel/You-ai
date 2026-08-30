from django.db import models

# --- Neon table placeholder   not migrated, not active yet ---
#
# Current auth is session-only, no user table at all (see accounts/views.py).
# This is the shape it'll need once real signup replaces the stub, including
# the fields that feed the personality space (see roadmap section 3).

# class UserProfile(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True, null=True, blank=True)  # null for now if email/password auth isn't decided yet
#     # onboarding_answers = models.JSONField(default=dict)   # raw questionnaire responses from signup
#     # personality_profile = models.JSONField(default=dict)  # derived tone/style profile, see chat/services/personality.py
#     created_at = models.DateTimeField(auto_now_add=True)
