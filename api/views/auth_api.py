from django.contrib.auth import login, authenticate
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from api.models import User

@csrf_exempt
@require_http_methods(["POST"])
def signup_api(request: HttpRequest) -> JsonResponse:
    """API endpoint for user signup"""
    try:
        body = json.loads(request.body.decode("utf-8") or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"ok": False, "error": "Invalid JSON"}, status=400)

    username: str = body.get("username", "").strip()
    email: str = body.get("email", "").strip()
    password: str = body.get("password", "").strip()
    date_of_birth_str: str = body.get("date_of_birth", "").strip()

    if not username or not email or not password:
        return JsonResponse({"ok": False, "error": "Missing required fields"}, status=400)
    
    if not date_of_birth_str:
        return JsonResponse({"ok": False, "error": "Date of birth is required"}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({"ok": False, "error": "Username already exists"}, status=400)

    if User.objects.filter(email=email).exists():
        return JsonResponse({"ok": False, "error": "Email already exists"}, status=400)

    try:
        date_of_birth = datetime.strptime(date_of_birth_str, "%Y-%m-%d").date()
    except ValueError:
        return JsonResponse({"ok": False, "error": "Invalid date format. Use YYYY-MM-DD"}, status=400)

    try:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.date_of_birth = date_of_birth
        user.save()
    except Exception as e:
        return JsonResponse({"ok": False, "error": f"Failed to create user: {str(e)}"}, status=500)
    
    # This ensures proper flow: signup -> login page -> login -> home
    
    return JsonResponse({
        "ok": True,
        "message": "Account created successfully. Please login.",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "date_of_birth": user.date_of_birth.isoformat() if user.date_of_birth else None,
        }
    }, status=201)


@csrf_exempt
@require_http_methods(["POST"])
def login_api(request: HttpRequest) -> JsonResponse:
    """API endpoint for user login"""
    try:
        body = json.loads(request.body.decode("utf-8") or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"ok": False, "error": "Invalid JSON"}, status=400)

    username: str = body.get("username", "").strip()
    password: str = body.get("password", "").strip()

    if not username or not password:
        return JsonResponse({"ok": False, "error": "Missing credentials"}, status=400)

    user = authenticate(request, username=username, password=password)
    
    if user is None:
        return JsonResponse({"ok": False, "error": "Invalid credentials"}, status=401)

    login(request, user)
    
    date_of_birth_value: str | None = None
    if user.date_of_birth:
        if hasattr(user.date_of_birth, 'isoformat'):
            date_of_birth_value = user.date_of_birth.isoformat()
        else:
            date_of_birth_value = str(user.date_of_birth)
    
    return JsonResponse({
        "ok": True,
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "date_of_birth": date_of_birth_value,
            "profile_image_url": user.profile_image.url if user.profile_image else None,
        }
    })


@csrf_exempt
@require_http_methods(["POST"])
def logout_api(request: HttpRequest) -> JsonResponse:
    """API endpoint for user logout"""
    from django.contrib.auth import logout
    logout(request)
    return JsonResponse({"ok": True})
