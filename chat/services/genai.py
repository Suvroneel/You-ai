"""
chat/services/genai.py

This is where You_AI's replies get generated. Structurally it mirrors
Phynix's PhynixAI class, but the intent behind it is different: Ashva was
a companion with its own fixed personality. You_AI is not a companion —
it's meant to sound like an extension of the person talking to it.

Right now the system prompt is a neutral, adaptive-tone placeholder.
It nudges the model to mirror the user's own tone back at them (formal,
sarcastic, blunt, warm, whatever comes through in their messages) rather
than layering on a separate assistant personality.

# TODO: personality profile injection
# Once the signup flow collects the psychological/preference questions
# (nickname, hypothetical-situation answers, values questions, etc.),
# that profile should be fetched here and folded into SYSTEM_PROMPT as
# structured context — e.g. "This user tends to be direct and dry, avoid
# corporate/spong tone, keep replies short." That's a separate research
# branch (personality modeling) and isn't wired in yet.
"""
from django.conf import settings


class YouAI:
    BASE_SYSTEM_PROMPT = """You are You_AI, a personal extension of the user — not a companion, not an assistant with its own personality. Your job is to sound like an extension of how THIS person talks and thinks, not like a generic helpful chatbot.

Rules:
- Mirror the user's tone. If their messages are warm and casual, be warm and casual. If they're blunt, sarcastic, or formal, match that register instead of defaulting to a "helpful assistant" voice.
- Do not perform empathy or add filler you wouldn't naturally hear from the user's own inner voice.
- Keep replies proportionate to the user's own message length and energy — don't pad short messages with long responses.
- Never claim to be human, and never pretend to have memories or context you have not actually been given.
- No emojis."""

    def __init__(self):
        from huggingface_hub import InferenceClient
        self.client = InferenceClient(token=getattr(settings, "HF_TOKEN", None))
        self.model = "meta-llama/Llama-3.1-8B-Instruct"

    def generate_response(self, user_message, chat_history=None, personality_context=None,
                           max_tokens=300, temperature=0.7):
        try:
            system_prompt = self.BASE_SYSTEM_PROMPT
            if personality_context:
                # TODO: this is the hook described above — currently unused
                system_prompt += f"\n\n[User personality context: {personality_context}]"

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
            return "Having a technical issue on my end. Try again in a second."
