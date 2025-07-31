from django.urls import path
from .views import PostView, post_detail

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('home/', PostView.as_view(), name='home_page'),
    path('<slug:slug>/', post_detail, name='post_detail'),
]
