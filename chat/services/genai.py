"""
chat/services/genai.py

This is where You_AI's replies get generated.
The system prompt establishes a warm, grounded, and naturally empathetic baseline.
It acts as a supportive alter-ego that feels human and approachable, designed
to seamlessly integrate future user personality injections.
"""
import os
from django.conf import settings
from huggingface_hub import InferenceClient


class YouAI:
    BASE_SYSTEM_PROMPT = """You are You_AI — a warm, grounded, and thoughtful personal extension of the user. You speak like a trusted peer and supportive alter-ego, not a cold software tool or a robotic script.

Core Conversational Principles:
- **Warmth & Empathy First:** Be naturally approachable, friendly, and empathetic. When the user greets you or shares thoughts, respond with genuine human warmth rather than pushback or sterile detachment.
- **Relatable & Natural Tone:** Talk naturally and conversationally. Avoid corporate jargon, robotic disclaimers ("As an AI..."), or unnatural artificial enthusiasm.
- **Proportional Energy:** Match the user's conversational pace. Keep short greetings brief and friendly, and match deeper conversations with thoughtful responses.
- **Supportive Framing:** Act as a collaborative sounding board. Be encouraging and insightful, helping the user brainstorm, edit, or navigate decisions smoothly.
- **Authentic Boundaries:** Be open and warm without being fake, overly sycophantic, or performative. Never use emojis."""

    def __init__(self):
        # Fallback to standard environment variables if settings.HF_TOKEN is missing
        token = getattr(settings, "HF_TOKEN", None) or os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACEHUB_API_KEY")

        # Initialize without forcing 'hf-inference' provider to prevent restrictive routing errors
        self.client = InferenceClient(token=token)
        self.model = "meta-llama/Llama-3.1-8B-Instruct"

    def generate_response(self, user_message, chat_history=None, personality_context=None,
                           max_tokens=300, temperature=0.7):
        try:
            system_prompt = self.BASE_SYSTEM_PROMPT
            if personality_context:
                system_prompt += f"\n\n[User personality nuances to layer in: {personality_context}]"

            messages = [{"role": "system", "content": system_prompt}]
            if chat_history:
                messages.extend(chat_history)
            messages.append({"role": "user", "content": user_message})

            resp = self.client.chat_completion(
                model=self.model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return resp.choices[0].message.content.strip()

        except Exception as e:
            err = str(e).lower()
            if "rate limit" in err:
                return "Getting a lot of traffic right now — try again in a moment."
            # TEMP DIAGNOSTIC — remove once bug is found
            return f"⚠️ DEBUG: {type(e).__name__}: {str(e)}"