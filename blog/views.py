from django.shortcuts import render
from .models import Post

def blog_post(request):
    blog_posts = Post.objects.filter(status=1).order_by('-created_on')

    context = {
        'blog_posts': blog_posts
    }

    return render(request, 'blog/blog.html')
