import json

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_http_methods, require_POST

from api.models import Item, Question, Reply, Notification


def question_to_dict(q: Question) -> dict:
    reply = getattr(q, "reply", None)
    return {
        "id": q.id,
        "item_id": q.item_id,
        "asker": {"id": q.asker_id, "username": q.asker.username},
        "text": q.text,
        "created_at": q.created_at.isoformat(),
        "reply": {
            "id": reply.id,
            "owner": {"id": reply.owner_id, "username": reply.owner.username},
            "text": reply.text,
            "created_at": reply.created_at.isoformat(),
        }
        if reply
        else None,
    }


@login_required
@require_http_methods(["GET", "POST"])
def item_questions_view(request: HttpRequest, item_id: int) -> JsonResponse:
    try:
        item = Item.objects.select_related("owner").get(id=item_id)
    except Item.DoesNotExist:
        return JsonResponse({"ok": False, "error": "Item not found"}, status=404)

    if request.method == "GET":
        questions = (
            Question.objects.filter(item=item)
            .select_related("asker")
            .prefetch_related("reply__owner")
            .order_by("-created_at")
        )
        return JsonResponse({"ok": True, "questions": [question_to_dict(q) for q in questions]})

    # POST: create question
    try:
        body = json.loads(request.body.decode("utf-8") or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"ok": False, "error": "Invalid JSON"}, status=400)

    text = str(body.get("text", "")).strip()
    if not text:
        return JsonResponse({"ok": False, "error": "Question text required"}, status=400)

    q = Question.objects.create(item=item, asker=request.user, text=text)  # type: ignore[arg-type]
    
    Notification.objects.create(
        user=item.owner,
        notification_type='question',
        title='New Question on Your Item',
        message=f'{request.user.username} asked: "{text[:50]}..."',
        link=f'/item/{item_id}'
    )
    
    return JsonResponse({"ok": True, "question": question_to_dict(q)}, status=201)


@login_required
@require_POST
def reply_view(request: HttpRequest, question_id: int) -> JsonResponse:
    try:
        body = json.loads(request.body.decode("utf-8") or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"ok": False, "error": "Invalid JSON"}, status=400)

    text = str(body.get("text", "")).strip()
    if not text:
        return JsonResponse({"ok": False, "error": "Reply text required"}, status=400)

    try:
        q = Question.objects.select_related("item", "item__owner", "asker").get(id=question_id)
    except Question.DoesNotExist:
        return JsonResponse({"ok": False, "error": "Question not found"}, status=404)

    if q.item.owner_id != request.user.id:
        return JsonResponse({"ok": False, "error": "Only the item owner can reply to this question"}, status=403)

    if hasattr(q, "reply"):
        return JsonResponse({"ok": False, "error": "This question has already received a reply"}, status=400)

    reply = Reply.objects.create(question=q, owner=request.user, text=text)  # type: ignore[arg-type]
    
    Notification.objects.create(
        user=q.asker,
        notification_type='reply',
        title='Your Question Was Answered',
        message=f'Seller replied: "{text[:50]}..."',
        link=f'/item/{q.item_id}'
    )
    
    return JsonResponse({"ok": True, "reply": {"id": reply.id, "text": reply.text}})
