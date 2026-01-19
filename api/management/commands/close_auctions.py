from __future__ import annotations

import logging
from django.core.management.base import BaseCommand
from django.utils import timezone

from api.services.auctions import close_ended_auctions
from api.models import Item

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Close ended auctions and email winners. Run via cron job every 5 minutes."

    def add_arguments(self, parser) -> None:
        parser.add_argument("--limit", type=int, default=200)
        parser.add_argument(
            "--verbose",
            action="store_true",
            help="Print detailed information about each auction being closed"
        )
        parser.add_argument(
            "--dry-run",
            action="store_true", 
            help="Show what would be closed without actually closing"
        )

    def handle(self, *args, **options) -> None:
        limit: int = options["limit"]
        verbose: bool = options["verbose"]
        dry_run: bool = options["dry_run"]
        
        now = timezone.now()
        self.stdout.write(f"[{now.isoformat()}] Running close_auctions command...")
        
        # Show pending auctions
        pending = Item.objects.filter(is_closed=False, ends_at__lte=now).count()
        self.stdout.write(f"Found {pending} auction(s) ready to close")
        
        if verbose or dry_run:
            auctions_to_close = Item.objects.filter(
                is_closed=False, 
                ends_at__lte=now
            ).select_related('owner').prefetch_related('bids')[:limit]
            
            for item in auctions_to_close:
                top_bid = item.bids.order_by('-amount').first()
                winner_info = f"Winner: {top_bid.bidder.username} (${top_bid.amount})" if top_bid else "No bids"
                self.stdout.write(f"  - '{item.title}' by {item.owner.username} | {winner_info}")
        
        if dry_run:
            self.stdout.write(self.style.WARNING("DRY RUN - No auctions were actually closed"))
            return
        
        closed = close_ended_auctions(limit=limit)
        
        if closed > 0:
            self.stdout.write(self.style.SUCCESS(f"Successfully closed {closed} auction(s) and sent winner emails"))
            logger.info(f"Closed {closed} auctions at {now.isoformat()}")
        else:
            self.stdout.write("No auctions needed closing")
