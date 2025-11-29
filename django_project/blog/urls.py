'''
    imported PostListView to be used for the home page
    updated the path for the home page to use PostListView.as_view()

    
'''
from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    path('',PostListView.as_view(), name='realty-home'),
    path('about/', views.about, name='realty-about'),
]
