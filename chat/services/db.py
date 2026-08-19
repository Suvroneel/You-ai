# chat/services/db.py
#
# STUB — not implemented. No logic below, only structure + comments.
#
# Purpose:
#   Once DATABASES points at Neon (see you_ai/settings.py) and the models
#   in chat/models.py are uncommented + migrated, chat/views.py should
#   call these instead of touching request.session directly. Keeping the
#   session-based version working right now, this is just the shape of
#   what replaces it.
#
# Mirrors Phynix's chat/services/db.py, but using the Django ORM against
# Neon instead of raw Supabase client calls.

# from .models import ChatMessage

# def save_message(user_id: str, sender: str, content: str):
#     """
#     Writes one message row. Called twice per turn from send_message()
#     in views.py — once for the user's message, once for the reply.
#     """
#     pass


# def get_chat_history(user_id: str, limit: int = 50) -> list:
#     """
#     Replaces request.session.get("chat_messages", []).
#     Returns messages in the same {"sender": ..., "content": ...} shape
#     the templates already expect, so chat.html / _message.html don't
#     need to change when this gets wired in.
#     """
#     pass


# def clear_history(user_id: str):
#     """
#     Replaces the session-clear in new_chat() in views.py.
#     """
#     pass
