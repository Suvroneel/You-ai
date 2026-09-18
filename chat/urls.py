from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path("", views.chat_view, name="chat"),
    path("send/", views.send_message, name="send_message"),
    path("new/", views.new_chat, name="new_chat"),
    path("overview/", views.overview_view, name="overview"),
    path("persona/", views.persona_view, name="persona"),
    path("perception/", views.perception_view, name="perception"),
    path("outreach/", views.outreach_view, name="outreach"),
]