from django.urls import path
from .views import news_feed

urlpatterns = [
    path("news-feed/", news_feed, name="news-feed"),
]
