from django.shortcuts import render, get_object_or_404
from .models import Post


def blog_post(request):
    """ Allows users to add new blog posts to blog page """
    post_list = Post.objects.filter(status=1).order_by('-created_on')

    context = {
        'post_list': post_list,
    }

    return render(request, 'blog/blog.html', context)


def post_detail(request, slug):
    """ Page allows users to see blog post and leave comments """
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)

    return render(request, template_name, {'post': post,})
