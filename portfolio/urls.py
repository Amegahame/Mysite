from django.urls import path
from .views import hello_view, post_view, home_view

urlpatterns = [
    path('', home_view, name='home'),          
    path('hello/', hello_view, name='hello_view'),
    path('post/', post_view, name='post_view'),
]
