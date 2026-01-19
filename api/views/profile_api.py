from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_http_methods

from api.models import User

@login_required
@require_http_methods(["GET", "POST"])
def me_view(request: HttpRequest) -> JsonResponse:
    user: User = request.user  # type: ignore[assignment]

    if request.method == "GET":
        return JsonResponse({
            "ok": True,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "date_of_birth": user.date_of_birth.isoformat() if user.date_of_birth else None,
                "profile_image_url": user.profile_image.url if user.profile_image else None,
            }
        })

    # POST update (multipart for image OR JSON)
    if request.content_type and request.content_type.startswith("multipart/form-data"):
        email = request.POST.get("email")
        dob = request.POST.get("date_of_birth")

        if email is not None:
            user.email = email
        if dob:
            user.date_of_birth = datetime.fromisoformat(dob).date()
        if "profile_image" in request.FILES:
            user.profile_image = request.FILES["profile_image"]

        user.save()
        return JsonResponse({"ok": True})

    # JSON fallback
    import json
    body = json.loads(request.body.decode("utf-8") or "{}")
    if "email" in body:
        user.email = str(body["email"])
    if body.get("date_of_birth"):
        user.date_of_birth = datetime.fromisoformat(str(body["date_of_birth"])).date()

    user.save()
    return JsonResponse({"ok": True})
