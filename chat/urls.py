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

    # Outreach Sub-routes
    path("outreach/", views.outreach_hub, name="outreach"),
    path("outreach/email/", views.outreach_email, name="outreach_email"),
    path("outreach/messages/", views.outreach_messages, name="outreach_messages"),
]