"""
accounts/views.py

STUB AUTH   deliberately minimal.
No password, no email verification, no OAuth. Just a name, stored in session.

Real auth (signup flow with the psychological/personality questions that
will shape each user's GenAI tone) is a separate, larger piece of work and
gets built later. This exists purely so the chat page has a `username` to
personalize around.
"""
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST


def login_view(request):
    if request.session.get("username"):
        return redirect("chat:chat")

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        if not name:
            return render(request, "accounts/login.html", {"error": "Enter a name to continue."})

        request.session["username"] = name
        request.session["logged_in"] = True
        request.session.modified = True
        return redirect("chat:chat")

    return render(request, "accounts/login.html", {})


@require_POST
def logout_view(request):
    request.session.flush()
    return redirect("accounts:login")
