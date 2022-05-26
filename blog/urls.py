from . import views
from django.urls import path

urlpatterns = [
    path('', views.blog_post, name="blog_post"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
