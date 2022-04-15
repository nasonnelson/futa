from django.urls import path
from . import views

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('contact/', views.contact.as_view(), name='contact'),
    path('video/', views.video.as_view(), name='video'),
    path('photo/', views.photo.as_view(), name='photo'),
    path('member/', views.member.as_view(), name='member'),
    path('about/', views.about.as_view(), name='about')
]