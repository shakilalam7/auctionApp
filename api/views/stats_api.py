from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from django.db.models import Sum

from api.models import Item, Bid


@login_required
@require_http_methods(["GET"])
def user_stats_view(request: HttpRequest) -> JsonResponse:
    """Get stats for the current user: active auctions, total bids, total spent"""
    user = request.user
    
    # Count active auctions (items the user is bidding on that are still active)
    user_bids = Bid.objects.filter(bidder=user).select_related('item')
    active_item_ids = set()
    for bid in user_bids:
        if not bid.item.is_closed and bid.item.ends_at > timezone.now():
            active_item_ids.add(bid.item.id)
    
    active_auctions = len(active_item_ids)
    
    # Total bids placed by user
    total_bids = Bid.objects.filter(bidder=user).count()
    
    # Total spent (sum of winning bids on closed auctions)
    total_spent = Decimal('0.00')
    for bid in user_bids:
        item = bid.item
        if item.is_closed or item.has_ended():
            highest_bid = item.current_highest_bid()
            if highest_bid and highest_bid.bidder_id == user.id:
                total_spent += highest_bid.amount
    
    return JsonResponse({
        'ok': True,
        'stats': {
            'active_auctions': active_auctions,
            'total_bids': total_bids,
            'total_spent': str(total_spent),
        }
    })
