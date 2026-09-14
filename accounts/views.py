from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def nickname_view(request):
    """
    Onboarding step after successful Google OAuth authentication.
    Captures the user's preferred nickname and stores it in session/user context.
    """
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
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

        # Optionally attach nickname to user first_name if desired
        request.user.first_name = name
        request.user.save(update_fields=["first_name"])

        return redirect("chat:chat")

    # If nickname is already set in session, prepopulate or proceed directly
    existing_name = request.session.get("username", request.user.first_name or "")

    return render(request, "accounts/nickname.html", {"existing_name": existing_name})


def logout_view(request):
    """
    Clears both Django user authentication and custom session variables.
    """
    logout(request)
    return redirect("account_login")
