from __future__ import annotations

from decimal import Decimal
from typing import Optional

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    email = models.EmailField(blank=False)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to="profiles/", null=True, blank=True)

    def __str__(self) -> str:
        return self.username


class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")
    title = models.CharField(max_length=200)
    description = models.TextField()
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="items/", null=True, blank=True)
    ends_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    is_closed = models.BooleanField(default=False)
    winner = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="wins"
    )
    final_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    winner_emailed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def has_ended(self) -> bool:
        return timezone.now() >= self.ends_at

    def current_highest_bid(self) -> Optional["Bid"]:
        return self.bids.order_by("-amount", "created_at").first()

    def current_price(self) -> Decimal:
        top = self.current_highest_bid()
        return top.amount if top else self.starting_price


class Bid(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="bids")
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-amount", "created_at"]

    def __str__(self) -> str:
        return f"{self.bidder.username} -> {self.item.title}: {self.amount}"


class Question(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="questions")
    asker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Q on {self.item.title} by {self.asker.username}"


class Reply(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name="reply")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="replies")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Reply by {self.owner.username}"


class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('question', 'New Question'),
        ('reply', 'Question Replied'),
        ('bid', 'New Bid'),
        ('outbid', 'Outbid'),
        ('won', 'Auction Won'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    title = models.CharField(max_length=200)
    message = models.TextField()
    link = models.CharField(max_length=200, null=True, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.user.username}: {self.title}"
