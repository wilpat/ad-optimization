from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='ads-home'),
    path('like/<int:ad>', views.like, name ='like-ad'),
    path('dislike/<int:ad>', views.dislike, name ='dislike-ad')
]