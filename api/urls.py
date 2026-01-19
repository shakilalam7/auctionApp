"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path

from api.views.spa import main_spa
from api.views.auth_pages import signup_view, login_view, logout_view
from api.views.auth_api import signup_api, login_api, logout_api
from api.views.csrf import csrf_view
from api.views.profile_api import me_view
from api.views.items_api import items_view, item_detail_view
from api.views.bids_api import place_bid_view, my_bids_view
from api.views.questions_api import item_questions_view, reply_view
from api.views.notifications_api import notifications_view, mark_notification_read_view, mark_all_notifications_read_view
from api.views.stats_api import user_stats_view  # Import the new stats view

urlpatterns = [
    # Auth pages (templates)
    path("signup/", signup_view),
    path("login/", login_view),
    path("logout/", logout_view),

    # CSRF helper
    path("api/csrf/", csrf_view),

    # Auth API
    path("api/auth/signup/", signup_api),
    path("api/auth/login/", login_api),
    path("api/auth/logout/", logout_api),
    path("api/logout/", logout_api),

    # API
    path("api/me/", me_view),
    path("api/items/", items_view),
    path("api/items/<int:item_id>/", item_detail_view),
    
    path("api/bids/", my_bids_view),
    path("api/items/<int:item_id>/bids/", place_bid_view),
    
    path("api/items/<int:item_id>/questions/", item_questions_view),
    path("api/questions/<int:question_id>/reply/", reply_view),
    
    path("api/notifications/", notifications_view),
    path("api/notifications/<int:notification_id>/read/", mark_notification_read_view),
    path("api/notifications/mark-all-read/", mark_all_notifications_read_view),
    
    path("api/stats/", user_stats_view),  # Add stats API endpoint
    
    # SPA fallback (Vue router refresh support) — keep last
    re_path(r"^(?!api/|admin/|health).*$", main_spa),
]

