from django.urls import path

from posts import views

app_name = 'posts'
urlpatterns = [
    path('post-list/', views.post_list_view, name='post-list'),
    path('create/', views.post_create_view, name='post-create'),
    path('detail/', views.post_detail_view, name='post-detail'),
    path('<int:pk>/like/', views.post_like_view, name='post-like'),
    path('<int:post_pk>/comment/', views.post_comment_view, name='post-comment'),

]
