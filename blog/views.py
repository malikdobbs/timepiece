from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_post(request):
    post_list = Post.objects.filter(status=1).order_by('-created_on')

    context = {
        'post_list': post_list,
    }

    return render(request, 'blog/blog.html', context)
