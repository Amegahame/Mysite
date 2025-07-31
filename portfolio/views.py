from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic

from .models.post import Post
from .forms import CommentForm

class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'post_list'  # seu index.html usa post_list

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by('-created_on')
    new_comment = None

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            # evita re-envio do form ao dar refresh
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(
        request,
        'post_detail.html',
        {
            'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': form,
        },
    )
