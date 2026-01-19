from __future__ import annotations

from typing import Optional

from django.conf import settings
from django.core.mail import send_mail
from django.db import transaction
from django.utils import timezone

from api.models import Bid, Item, User, Notification


def _highest_bid(item: Item) -> Optional[Bid]:
    return item.bids.select_related("bidder").order_by("-amount", "created_at").first()


@transaction.atomic
def close_one_item(item: Item) -> bool:
    """
    Close a single item if it's ended and not already closed.
    Returns True if it was closed during this call, False otherwise.
    """
    # lock row so cron isn't racing with itself
    item = Item.objects.select_for_update().select_related("owner").get(id=item.id)

    if item.is_closed:
        return False
    if item.ends_at > timezone.now():
        return False

    top = _highest_bid(item)

    item.is_closed = True

    if top is None:
        # No bids: close without winner + no email
        item.winner = None
        item.final_price = None
        item.winner_emailed_at = None
        item.save(update_fields=["is_closed", "winner", "final_price", "winner_emailed_at"])
        return True

    winner: User = top.bidder
    item.winner = winner
    item.final_price = top.amount

    Notification.objects.create(
        user=winner,
        notification_type='won',
        title='Congratulations! You Won the Auction',
        message=f'You won "{item.title}" with a bid of ${top.amount}. Check your email for details.',
        link=f'/item/{item.id}'
    )

    # email exactly once
    if item.winner_emailed_at is None:
        subject = f"You won the auction: {item.title}"
        message = (
            f"Congratulations {winner.username}!\n\n"
            f"You won '{item.title}' with a bid of {top.amount}.\n"
            f"Please proceed to purchase the item.\n\n"
            f"Auction ended at: {item.ends_at.isoformat()}\n"
        )
        from_email = getattr(settings, "DEFAULT_FROM_EMAIL", None) or getattr(settings, "EMAIL_HOST_USER", "")
        if from_email:
            send_mail(subject, message, from_email, [winner.email], fail_silently=False)
        item.winner_emailed_at = timezone.now()

    item.save(update_fields=["is_closed", "winner", "final_price", "winner_emailed_at"])
    return True


def close_ended_auctions(limit: int = 200) -> int:
    """
    Close up to `limit` auctions that have ended and are not closed.
    Returns the number of items closed.
    """
    qs = (
        Item.objects.filter(is_closed=False, ends_at__lte=timezone.now())
        .order_by("ends_at")[:limit]
    )

    closed = 0
    for item in qs:
        if close_one_item(item):
            closed += 1
    return closed
