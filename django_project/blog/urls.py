from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='realty-home'),
    path('about/', views.about, name='realty-about'),
]
