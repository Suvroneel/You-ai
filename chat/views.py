from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from accounts.decorators import login_required


@login_required
def chat_view(request):
    messages = request.session.get("chat_messages", [])
    context = {
        "messages": messages,
        "username": request.session.get("username", "there"),
    }
    return render(request, "chat/chat.html", context)


@login_required
@require_POST
def send_message(request):
    from .services.genai import YouAI

    text = request.POST.get("message", "").strip()
    if not text:
        return HttpResponse("")

    session_msgs = request.session.get("chat_messages", [])
    chat_history = [
        {"role": "user" if m["sender"] == "user" else "assistant", "content": m["content"]}
        for m in session_msgs
    ]

    ai = YouAI()
    reply = ai.generate_response(
        user_message=text,
        chat_history=chat_history,
    )

    session_msgs.append({"sender": "user", "content": text})
    session_msgs.append({"sender": "bot", "content": reply})
    request.session["chat_messages"] = session_msgs
    request.session.modified = True

    user_html = render(request, "chat/_message.html", {"msg": {"sender": "user", "content": text}}).content.decode()
    bot_html = render(request, "chat/_message.html", {"msg": {"sender": "bot", "content": reply}}).content.decode()
    return HttpResponse(user_html + bot_html)


@login_required
@require_POST
def new_chat(request):
    request.session["chat_messages"] = []
    request.session.modified = True
    return HttpResponse("")
