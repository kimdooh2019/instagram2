from django.urls import path

from members import views

app_name='members'
urlpatterns = [
    path('', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
]