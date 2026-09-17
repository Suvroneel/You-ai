from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from chat.models import UserPersonality
from accounts.models import GoogleUser


@login_required
def nickname_view(request):
    """
    Onboarding step after successful Google OAuth authentication.
    Captures the user's preferred nickname and stores it in session/user context.
    """
    if request.method == "POST":
        name = (request.POST.get("nickname") or request.POST.get("name") or "").strip()
        if not name:
            return render(
                request,
                "accounts/nickname.html",
                {"error": "Please enter a nickname to continue."}
            )

        # Store in session for chat personalization
        request.session["username"] = name
        request.session["logged_in"] = True
        request.session.modified = True

        # Attach nickname to user first_name
        request.user.first_name = name
        request.user.save(update_fields=["first_name"])

        return redirect("accounts:personality_setup")

    existing_name = request.session.get("username", request.user.first_name or "")
    return render(request, "accounts/nickname.html", {"existing_name": existing_name})


@login_required
def personality_setup_view(request):
    """
    Onboarding step 2: Captures tone preferences (Warm, Sarcastic, Enthusiastic)
    and communication style (Casual, Direct).
    """
    try:
        google_user = GoogleUser.objects.get(email=request.user.email)
    except GoogleUser.DoesNotExist:
        google_user, _ = GoogleUser.objects.get_or_create(
            email=request.user.email,
            defaults={"name": request.user.first_name or "User", "google_sub": str(request.user.id)}
        )

    personality, _ = UserPersonality.objects.get_or_create(user=google_user)

    if request.method == "POST":
        selected_tones = request.POST.getlist("tones")
        tone_preference_str = ", ".join(selected_tones) if selected_tones else "Warm"
        comm_style = request.POST.get("communication_style", "Casual")

        personality.tone_preference = tone_preference_str
        personality.communication_style = comm_style
        personality.save()

        request.session["personality_setup_complete"] = True
        request.session.modified = True

        return redirect("/chat/")

    return render(request, "accounts/personality_setup.html", {
        "current_tone": personality.tone_preference or "",
        "current_style": personality.communication_style or "Casual"
    })


@login_required
def settings_view(request):
    """
    Settings view to edit nickname, tone preferences, and communication style.
    """
    try:
        google_user = GoogleUser.objects.get(email=request.user.email)
    except GoogleUser.DoesNotExist:
        google_user, _ = GoogleUser.objects.get_or_create(
            email=request.user.email,
            defaults={"name": request.user.first_name or "User", "google_sub": str(request.user.id)}
        )

    personality, _ = UserPersonality.objects.get_or_create(user=google_user)

    if request.method == "POST":
        name = (request.POST.get("nickname") or request.POST.get("name") or "").strip()
        if name:
            request.session["username"] = name
            request.session.modified = True
            request.user.first_name = name
            request.user.save(update_fields=["first_name"])
            google_user.name = name
            google_user.save(update_fields=["name"])

        selected_tones = request.POST.getlist("tones")
        personality.tone_preference = ", ".join(selected_tones) if selected_tones else "Warm"

        comm_style = request.POST.get("communication_style", "Casual")
        personality.communication_style = comm_style
        personality.save()

        return render(request, "accounts/settings.html", {
            "current_name": request.user.first_name or "",
            "current_tone": personality.tone_preference or "",
            "current_style": personality.communication_style or "Casual",
            "success_message": "Settings updated successfully!"
        })

    return render(request, "accounts/settings.html", {
        "current_name": request.user.first_name or request.session.get("username", ""),
        "current_tone": personality.tone_preference or "",
        "current_style": personality.communication_style or "Casual"
    })


def logout_view(request):
    """
    Clears both Django user authentication and custom session variables.
    """
    logout(request)
    return redirect("account_login")