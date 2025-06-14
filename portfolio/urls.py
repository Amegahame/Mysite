from django.urls import path
from .views import PostView, PostDetail

urlpatterns = [
    path('', PostView.as_view(), name='home'),           # Home na raiz
    path('home/', PostView.as_view(), name='home_page'), # Home acessível também por /home
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
