from django.http import HttpResponse
from django.shortcuts import render
from portfolio.models import Post

def hello_view(request):
    return HttpResponse("Hello World!")

def home_view(request):
    return HttpResponse("Página inicial")

def post_view(request):
    post = Post.objects.first()
    context = {
        'post': post,
    }
    return render(request, 'post_detail.html', context)
