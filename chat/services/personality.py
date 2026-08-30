# chat/services/personality.py
#
# STUB   not implemented. No logic below, only structure + comments.
# See YOU_AI_ROADMAP.md section 3 for the full explanation.
#
# Purpose:
#   Builds and retrieves the "personality profile" for a user   the thing
#   that eventually gets passed into YouAI.generate_response() as
#   `personality_context` (see the TODO marker in chat/services/genai.py).
#
# Planned functions (signatures only   do not implement yet):

# def build_profile_from_onboarding(user_id, questionnaire_answers: dict) -> dict:
#     """
#     Takes the signup questionnaire answers (nickname, tone self-description,
#     situational/hypothetical question responses) and turns them into a
#     structured profile: things like tone (warm / dry / blunt), typical
#     message length, humor style, directness.
#     Zero-cost approach: this can run entirely on the free HF Inference API
#     call (same Llama 3.1 endpoint already used for chat) with a prompt that
#     asks it to summarize traits from the answers   no extra paid service
#     needed for the first version.
#     Store result in Neon (Postgres) as a JSON column against the user.
#     """
#     pass


# def refresh_profile_from_recent_messages(user_id, message_limit=50) -> dict:
#     """
#     Periodically re-derives the voice profile from actual chat history
#     instead of relying only on the one-time onboarding answers.
#     Pulls last N messages from Neon, summarizes tone drift.
#     Zero-cost: reuse the same free Llama 3.1 HF Inference endpoint,
#     run as a scheduled/background job (e.g. Django management command
#     triggered by cron) rather than on every request.
#     """
#     pass


# def get_personality_context(user_id) -> str:
#     """
#     Fetches the stored profile (from Neon) and formats it into the short
#     string that gets injected into genai.py's `personality_context` param.
#     This is the function chat/views.py will actually call once this
#     exists   everything else here is what feeds it.
#     """
#     pass


# def embed_message_for_memory(user_id, text, source):
#     """
#     Same idea as Phynix's Utils/memory.py (sentence-transformers +
#     pgvector) but pointed at Neon instead of Supabase.
#     sentence-transformers (all-MiniLM-L6-v2) runs locally   zero cost,
#     no API calls needed for embeddings.
#     """
#     pass
