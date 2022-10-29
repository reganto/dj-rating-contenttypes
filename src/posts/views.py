from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from posts.models import Post

# Create your views here.


def post_list(
    request: HttpRequest,
) -> HttpResponse:
    """Post list view."""
    posts = Post.objects.order_by("created").all()
    return render(
        request,
        "posts/list.html",
        {
            "posts": posts,
        },
    )
