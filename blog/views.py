from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from .models import Post


def blog_post(request):
    """ Allows users to add new blog posts to blog page """
    post_list = Post.objects.filter(status=1).order_by('-created_on')

    context = {
        'post_list': post_list,
        'blog_page': 'active',
    }

    return render(request, 'blog/blog.html', context)


def post_detail(request, slug):
    """ Page allows users to see blog post and leave comments """
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
