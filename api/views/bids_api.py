import json
from decimal import Decimal, InvalidOperation
from typing import List, Dict, Any

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_http_methods
from api.models import Item, Bid, Notification

@login_required
@require_http_methods(["POST"])
def place_bid_view(request: HttpRequest, item_id: int) -> JsonResponse:
    try:
        body = json.loads(request.body.decode("utf-8") or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"ok": False, "error": "Invalid JSON"}, status=400)

    raw_amount = body.get("amount")
    
    try:
        amount = Decimal(str(raw_amount))
    except (InvalidOperation, TypeError):
        return JsonResponse({"ok": False, "error": "Invalid bid amount"}, status=400)
    
    try:
        item = Item.objects.select_related("owner").get(id=item_id)
    except Item.DoesNotExist:
        return JsonResponse({"ok": False, "error": "Item not found"}, status=404)
    
    if item.is_closed or item.has_ended():
        return JsonResponse({"ok": False, "error": "Auction has ended"}, status=400)
    
    current = item.current_price()
    if amount <= current:
        return JsonResponse(
            {"ok": False, "error": f"Bid must be greater than current price ({current})"},
            status=400
        )
    
    previous_highest = item.current_highest_bid()
    
    bid = Bid.objects.create(item=item, bidder=request.user, amount=amount)
    
    Notification.objects.create(
        user=item.owner,
        notification_type='bid',
        title='New Bid on Your Item',
        message=f'{request.user.username} placed a bid of ${amount} on "{item.title}"',
        link=f'/item/{item_id}'
    )
    
    if previous_highest and previous_highest.bidder != request.user:
        Notification.objects.create(
            user=previous_highest.bidder,
            notification_type='outbid',
            title='You Have Been Outbid',
            message=f'Someone placed a higher bid on "{item.title}". Current bid: ${amount}',
            link=f'/item/{item_id}'
        )
    
    return JsonResponse({
        "ok": True,
        "bid": {
            "id": bid.id,
            "amount": str(bid.amount),
            "item_id": item.id
        }
    })

@login_required
@require_http_methods(["GET"])
def my_bids_view(request: HttpRequest) -> JsonResponse:
    """Fetch all bids placed by the current user with item details"""
    bids = Bid.objects.filter(bidder=request.user).select_related('item', 'item__owner').order_by('-created_at')
    
    bid_list: List[Dict[str, Any]] = []
    for bid in bids:
        item = bid.item
        highest_bid = item.current_highest_bid()
        is_winning = highest_bid and highest_bid.id == bid.id
        
        bid_list.append({
            'id': bid.id,
            'amount': str(bid.amount),
            'is_winning': is_winning,
            'created_at': bid.created_at.isoformat(),
            'item': {
                'id': item.id,
                'title': item.title,
                'description': item.description,
                'image_url': item.image.url if item.image else None,
                'current_price': str(item.current_price()),
                'starting_price': str(item.starting_price),
                'ends_at': item.ends_at.isoformat(),
                'is_active': not item.is_closed and not item.has_ended(),
                'bid_count': item.bids.count(),
                'owner': {
                    'id': item.owner.id,
                    'username': item.owner.username,
                }
            }
        })
    
    return JsonResponse({
        'ok': True,
        'bids': bid_list
    })
