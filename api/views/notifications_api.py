from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_http_methods, require_POST

from api.models import Notification


def notification_to_dict(n: Notification) -> dict:
    return {
        "id": n.id,
        "type": n.notification_type,
        "title": n.title,
        "message": n.message,
        "link": n.link,
        "is_read": n.is_read,
        "created_at": n.created_at.isoformat(),
    }


@login_required
@require_http_methods(["GET"])
def notifications_view(request: HttpRequest) -> JsonResponse:
    notifications = Notification.objects.filter(user=request.user).order_by("-created_at")
    return JsonResponse({
        "ok": True,
        "notifications": [notification_to_dict(n) for n in notifications],
        "unread_count": notifications.filter(is_read=False).count()
    })


@login_required
@require_POST
def mark_notification_read_view(request: HttpRequest, notification_id: int) -> JsonResponse:
    try:
        notification = Notification.objects.get(id=notification_id, user=request.user)
        notification.is_read = True
        notification.save()
        return JsonResponse({"ok": True})
    except Notification.DoesNotExist:
        return JsonResponse({"ok": False, "error": "Notification not found"}, status=404)


@login_required
@require_POST
def mark_all_notifications_read_view(request: HttpRequest) -> JsonResponse:
    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    return JsonResponse({"ok": True})
