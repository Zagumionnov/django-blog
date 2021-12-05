from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone

from .models import Post
from .forms import PostForm


def post_list(request):
    """Displays all posts on the main page."""
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'my_blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    """view a specific post."""
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'my_blog/post_detail.html', {'post': post})


def post_new(request):
    """View for creating a new post."""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'my_blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    """View for editing post."""
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'my_blog/post_edit.html', {'form': form})
