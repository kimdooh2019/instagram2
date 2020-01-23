from django.urls import path

from posts import views

app_name = 'posts'
urlpatterns = [
    path('post-list/', views.post_list_view, name='post-list'),
    path('create/', views.post_create_view, name='create'),
    path('detail/', views.post_detail_view, name='detail'),
    path('post-like/', views.post_like_view, name='post-like'),
]
