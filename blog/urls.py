from django.urls import path
from .views import NewsListView, NewsDetailView, ArticleListView, ArticleDetailView

app_name = 'blog'

urlpatterns = [
    path("news/", NewsListView.as_view(), name="news_list"),
    path("news/<slug:slug>/", NewsDetailView.as_view(), name="news_detail"),
    path("articles/", ArticleListView.as_view(), name="article_list"),
    path("articles/<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),
]