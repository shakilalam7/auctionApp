import json
from decimal import Decimal
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.http import HttpRequest, JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_http_methods

from api.models import Item

def _item_to_dict(item: Item) -> dict:
    top = item.current_highest_bid()
    is_active = not item.is_closed and item.ends_at > timezone.now()
    
    return {
        "id": item.id,
        "title": item.title,
        "description": item.description,
        "starting_price": str(item.starting_price),
        "current_price": str(item.current_price()),
        "image_url": item.image.url if item.image else None,
        "ends_at": item.ends_at.isoformat(),
        "owner": {"id": item.owner_id, "username": item.owner.username},
        "is_active": is_active,
        "is_closed": item.is_closed,
        "bid_count": item.bids.count(),
        "highest_bid": {
            "id": top.id,
            "amount": str(top.amount),
            "bidder": {"id": top.bidder_id, "username": top.bidder.username},
            "created_at": top.created_at.isoformat(),
        } if top else None,
    }

@login_required
@require_http_methods(["GET", "POST"])
def items_view(request: HttpRequest) -> JsonResponse:
    if request.method == "GET":
        my_items = request.GET.get("my_items") == "true"
        q = (request.GET.get("q") or "").strip()
        
        if my_items:
            qs = Item.objects.filter(owner=request.user).select_related("owner").prefetch_related("bids")
        else:
            qs = Item.objects.filter(is_closed=False, ends_at__gt=timezone.now()).select_related("owner").prefetch_related("bids")
            if q:
                qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))
        
        return JsonResponse({"ok": True, "items": [_item_to_dict(i) for i in qs.order_by("-id")[:200]]})

    # Create item via multipart/FormData
    title = request.POST.get("title", "").strip()
    description = request.POST.get("description", "").strip()
    starting_price = request.POST.get("starting_price", "").strip()
    ends_at = request.POST.get("ends_at", "").strip()

    if not title or not description or not starting_price or not ends_at:
        return JsonResponse({"ok": False, "error": "Missing required fields."}, status=400)

    try:
        sp = Decimal(starting_price)
    except Exception:
        return JsonResponse({"ok": False, "error": "Invalid starting_price."}, status=400)

    try:
        end_dt = datetime.fromisoformat(ends_at.replace('T', ' '))
        if timezone.is_naive(end_dt):
            end_dt = timezone.make_aware(end_dt, timezone.get_current_timezone())
    except Exception as e:
        return JsonResponse({"ok": False, "error": f"Invalid ends_at format: {str(e)}"}, status=400)

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
        return JsonResponse({"ok": False, "error": "Item not found"}, status=404)
    return JsonResponse({"ok": True, "item": _item_to_dict(item)})
