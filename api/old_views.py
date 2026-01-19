"""Views for the auction app."""

from __future__ import annotations

import json
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import Q
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods

from .models import Bid, Item, Question, Reply, User


# -------------------------
# Helpers / serialization
# -------------------------

def _json_error(message: str, status: int = 400) -> JsonResponse:
    return JsonResponse({"ok": False, "error": message}, status=status)


def _item_to_dict(item: Item) -> Dict[str, Any]:
    top = item.current_highest_bid()
    return {
        "id": item.id,
        "owner": {"id": item.owner_id, "username": item.owner.username},
        "title": item.title,
        "description": item.description,
        "starting_price": str(item.starting_price),
        "current_price": str(item.current_price()),
        "image_url": item.image.url if item.image else None,
        "ends_at": item.ends_at.isoformat(),
        "is_closed": item.is_closed,
        "highest_bid": {
            "id": top.id,
            "amount": str(top.amount),
            "bidder": {"id": top.bidder_id, "username": top.bidder.username},
            "created_at": top.created_at.isoformat(),
        } if top else None,
    }


def _question_to_dict(q: Question) -> Dict[str, Any]:
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
        } if reply else None,
    }


def _get_json_body(request: HttpRequest) -> Dict[str, Any]:
    try:
        return json.loads(request.body.decode("utf-8") or "{}")
    except json.JSONDecodeError:
        return {}


# -------------------------
# Template pages (auth)
# -------------------------

def signup_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("/")

    # You can replace this with a custom form that asks DOB/profile_image/email
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user: User = form.save()  # type: ignore[assignment]
        login(request, user)
        return redirect("/")

    return render(request, "api/auth/signup.html", {"form": form})


def login_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("/")

    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("/")

    return render(request, "api/auth/login.html", {"form": form})


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("/login/")


@login_required
def main_spa(request: HttpRequest) -> HttpResponse:
    # Vue should only be accessible once authenticated (spec requirement)
    return render(request, "api/spa/index.html", {})


# -------------------------
# CSRF helper for Vue fetch
# -------------------------

@ensure_csrf_cookie
@require_http_methods(["GET"])
def csrf_view(request: HttpRequest) -> JsonResponse:
    # Just hitting this endpoint sets csrftoken cookie.
    return JsonResponse({"ok": True})


# -------------------------
# API: profile
# -------------------------

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

    # POST update (Ajax). Supports JSON or multipart (for image).
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

    body = _get_json_body(request)
    if "email" in body:
        user.email = str(body["email"])
    if "date_of_birth" in body and body["date_of_birth"]:
        user.date_of_birth = datetime.fromisoformat(str(body["date_of_birth"])).date()
    user.save()
    return JsonResponse({"ok": True})


# -------------------------
# API: items + search + create
# -------------------------

@login_required
@require_http_methods(["GET", "POST"])
def items_view(request: HttpRequest) -> JsonResponse:
    if request.method == "GET":
        q = (request.GET.get("q") or "").strip()

        items_qs = items_qs.filter(Q(title__icontains=q) | Q(description__icontains=q))
        if q:
            items_qs = items_qs.filter(models.Q(title__icontains=q) | models.Q(description__icontains=q))  # type: ignore[name-defined]

        items = [_item_to_dict(i) for i in items_qs.order_by("ends_at")[:200]]
        return JsonResponse({"ok": True, "items": items})

    # POST create item (multipart recommended  image)
    if not (request.content_type and request.content_type.startswith("multipart/form-data")):
        return _json_error("Expected multipart/form-data for item creation (use FormData).")

    title = request.POST.get("title", "").strip()
    description = request.POST.get("description", "").strip()
    starting_price = request.POST.get("starting_price", "").strip()
    ends_at = request.POST.get("ends_at", "").strip()

    if not title or not description or not starting_price or not ends_at:
        return _json_error("Missing required fields.")

    try:
        sp = Decimal(starting_price)
    except Exception:
        return _json_error("Invalid starting_price.")

    try:
        end_dt = datetime.fromisoformat(ends_at)
        if timezone.is_naive(end_dt):
            end_dt = timezone.make_aware(end_dt, timezone.get_current_timezone())
    except Exception:
        return _json_error("Invalid ends_at. Use ISO format.")

    item = Item.objects.create(
        owner=request.user,  # type: ignore[arg-type]
        title=title,
        description=description,
        starting_price=sp,
        ends_at=end_dt,
        image=request.FILES.get("image"),
    )
    return JsonResponse({"ok": True, "item": _item_to_dict(item)}, status=201)


@login_required
@require_http_methods(["GET"])
def item_detail_view(request: HttpRequest, item_id: int) -> JsonResponse:
    try:
        item = Item.objects.select_related("owner").get(id=item_id)
    except Item.DoesNotExist:
        return _json_error("Item not found.", status=404)

    return JsonResponse({"ok": True, "item": _item_to_dict(item)})


# -------------------------
# API: bidding
# -------------------------

@login_required
@require_http_methods(["POST"])
def place_bid_view(request: HttpRequest, item_id: int) -> JsonResponse:
    body = _get_json_body(request)
    amount_raw = body.get("amount")

    try:
        amount = Decimal(str(amount_raw))
    except Exception:
        return _json_error("Invalid bid amount.")

    try:
        item = Item.objects.select_related("owner").get(id=item_id)
    except Item.DoesNotExist:
        return _json_error("Item not found.", status=404)

    if item.is_closed or item.has_ended():
        return _json_error("Auction has ended.", status=400)

    current = item.current_price()
    if amount <= current:
        return _json_error(f"Bid must be greater than current price ({current}).", status=400)

    bid = Bid.objects.create(item=item, bidder=request.user, amount=amount)  # type: ignore[arg-type]
    return JsonResponse({"ok": True, "bid": {"id": bid.id, "amount": str(bid.amount)}})


# -------------------------
# API: questions + replies
# -------------------------

@login_required
@require_http_methods(["GET", "POST"])
def item_questions_view(request: HttpRequest, item_id: int) -> JsonResponse:
    try:
        item = Item.objects.select_related("owner").get(id=item_id)
    except Item.DoesNotExist:
        return _json_error("Item not found.", status=404)

    if request.method == "GET":
        qs = Question.objects.filter(item=item).select_related("asker").order_by("-created_at")
        data = [_question_to_dict(q) for q in qs]
        return JsonResponse({"ok": True, "questions": data})

    body = _get_json_body(request)
    text = str(body.get("text", "")).strip()
    if not text:
        return _json_error("Question text required.")

    q = Question.objects.create(item=item, asker=request.user, text=text)  # type: ignore[arg-type]
    return JsonResponse({"ok": True, "question": _question_to_dict(q)}, status=201)


@login_required
@require_http_methods(["POST"])
def reply_view(request: HttpRequest, question_id: int) -> JsonResponse:
    body = _get_json_body(request)
    text = str(body.get("text", "")).strip()
    if not text:
        return _json_error("Reply text required.")

    try:
        q = Question.objects.select_related("item", "item__owner").get(id=question_id)
    except Question.DoesNotExist:
        return _json_error("Question not found.", status=404)

    # only item owner can reply
    if q.item.owner_id != request.user.id:
        return _json_error("Only the item owner can reply.", status=403)

    # one reply per question (OneToOne)
    if hasattr(q, "reply"):
        return _json_error("This question already has a reply.", status=400)

    reply = Reply.objects.create(question=q, owner=request.user, text=text)  # type: ignore[arg-type]
    return JsonResponse({"ok": True, "reply": {"id": reply.id, "text": reply.text}})
