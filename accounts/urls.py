from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("nickname/", views.nickname_view, name="nickname"),
    path("personality/", views.personality_setup_view, name="personality_setup"),
    path("settings/", views.settings_view, name="settings"),
    path("logout/", views.logout_view, name="logout"),
]