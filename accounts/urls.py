from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("nickname/", views.nickname_view, name="nickname"),
    path("logout/", views.logout_view, name="logout"),
]