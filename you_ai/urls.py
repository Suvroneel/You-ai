from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(pattern_name="chat:chat"), name="root"),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("chat/", include("chat.urls", namespace="chat")),
]
