from tokenize import Name
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


# Create your views here.
def home(request):
    all_posts = Post.objects.all()
    name = 'ramu'
    context = {'posts': all_posts, "Name" : name}

    return render(request, 'home.html', context)

def post_single(request, post):
    post = get_object_or_404(Post, slug = post)
    return render(request, 'detail.html', {'post': post})

