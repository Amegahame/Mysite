from django.urls import path
from . import views 

urlpatterns = [
    path('', views.alguma_view, name='home'),   # ✅ rota principal
    path('post/', views.post_view, name='post_view'),  # ✅ rota /post/
]
