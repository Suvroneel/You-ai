from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(pattern_name="chat:chat"), name="root"),

    # Allauth URLs (handles /accounts/login/, /accounts/google/login/, callbacks)
    path("accounts/", include("allauth.urls")),

    # Custom App accounts URLs (handles /accounts/nickname/ and post-login onboarding)
    path("accounts/", include("accounts.urls", namespace="accounts")),

    # Chat app URLs
    path("chat/", include("chat.urls", namespace="chat")),
]