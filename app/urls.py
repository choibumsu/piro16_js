from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('api/get/comments', views.get_comments_api, name='get_comments_api'),
    path('api/post/comment', views.post_comment_api, name='post_comment_api'),
]
