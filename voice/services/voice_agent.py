# voice/services/voice_agent.py
#
# STUB   not implemented. No logic below, only structure + comments.
# See YOU_AI_ROADMAP.md section 4 (Multimodal) for context.
#
# Purpose:
#   Lets a user talk to You_AI instead of typing, and optionally hear a
#   reply back. Two halves: speech-to-text (in) and text-to-speech (out).
#
# Zero-cost approach:
#   - STT: faster-whisper running locally (same library Phynix already
#     used)   fully offline, no API cost, just needs CPU/GPU time.
#     Browser-side Web Speech API is an even cheaper fallback (runs in
#     the user's browser, no server cost at all) for supported browsers.
#   - TTS: options that stay at $0   Coqui TTS (local, open source) or
#     pyttsx3 (local, offline, lower quality but free). Avoid paid TTS
#     APIs (ElevenLabs etc.) unless budget changes later.

# def transcribe_audio(audio_file) -> str:
#     """
#     Mirrors Phynix's voice/views.py transcribe endpoint.
#     Runs faster-whisper locally on the uploaded audio blob, returns text.
#     That text then goes through the normal chat/send_message flow  
#     voice is just an alternate input method, not a separate pipeline.
#     """
#     pass


# def synthesize_speech(text: str) -> bytes:
#     """
#     Takes a You_AI text reply and turns it into audio using a local,
#     free TTS engine. Returned bytes get streamed back to the browser
#     as playable audio.
#     Not required for MVP   text-only replies are fine at first. This
#     is what makes it feel more like a call than a chat, later.
#     """
#     pass


# def handle_voice_turn(audio_file) -> dict:
#     """
#     Orchestrates one full voice turn: transcribe -> send through
#     YouAI.generate_response() (same as text chat) -> optionally
#     synthesize_speech() on the reply -> return both text + audio.
#     """
#     pass
