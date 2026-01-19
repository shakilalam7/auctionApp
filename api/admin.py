from django.contrib import admin
from .models import User, Item, Bid, Question, Reply

admin.site.register(User)
admin.site.register(Item)
admin.site.register(Bid)
admin.site.register(Question)
admin.site.register(Reply)
