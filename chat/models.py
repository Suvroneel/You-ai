from django.db import models

# --- Neon table placeholders   not migrated, not active yet ---
#
# Right now chat history lives in request.session only (see chat/views.py).
# These are commented out so the schema shape is decided in advance  
# uncomment + makemigrations once DATABASES points at Neon (see
# you_ai/settings.py for the connection placeholder).

# class ChatMessage(models.Model):
#     """
#     One row per message, mirrors what's currently stored in
#     request.session["chat_messages"].
#     """
#     user_id = models.CharField(max_length=255, db_index=True)  # ties to accounts user, once real auth exists
#     sender = models.CharField(max_length=10)  # "user" or "bot"
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ["created_at"]


# class MemoryEmbedding(models.Model):
#     """
#     Mirrors Phynix's memory_embeddings table (RAG pipeline), but on
#     Neon instead of Supabase. Neon supports pgvector natively.
#     See chat/services/personality.py -> embed_message_for_memory().
#     """
#     user_id = models.CharField(max_length=255, db_index=True)
#     source = models.CharField(max_length=20)  # "chat" / "diary" / etc.
#     text = models.TextField()
#     # embedding = VectorField(dimensions=384)  # needs pgvector Django field, e.g. django-pgvector
#     created_at = models.DateTimeField(auto_now_add=True)
