'''
    imported PostListView to be used for the home page
    updated the path for the home page to use PostListView.as_view()

    imported PostDetailView to be used for individual post detail pages
    loaded the path for individual post detail pages to use PostDetailView.as_view()
    pk is used to capture the primary key of the post from the URL

    import PostCreateView to be used for creating new posts
    added a path for creating new posts using PostCreateView.as_view()
    create a template for the post creation form at blog/post_form.html

    import PostUpdateView to be used for updating existing posts
    added a path for updating existing posts using PostUpdateView.as_view()

    import PostDeleteView to be used for deleting posts
    added a path for deleting posts using PostDeleteView.as_view()
    then proceed to create a template for the post deletion confirmation at blog/post_confirm_delete.html
'''
from django.urls import path 
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
from . import views

urlpatterns = [
    path('',PostListView.as_view(), name='realty-home'),
    path('user/<str:username>/',UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('post/new/',PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='realty-about'),
]
