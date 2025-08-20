from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('authors/<int:author_id>/posts', views.posts_by_author, name='posts_by_author'),
]