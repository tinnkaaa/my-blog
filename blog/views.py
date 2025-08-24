from django.shortcuts import render, get_object_or_404
from .models import Post, Author

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html", {"post": post})

def posts_by_author(request, author_id):
    author = Author.objects.filter(pk=author_id).first()
    posts = Post.objects.filter(author=author)
    return render(request, 'posts_by_author.html', {"author": author, 'posts': posts})