from api.v1.serializers import PostSerializer
from posts.models import Post
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import HttpRequest
from rest_framework.response import Response


@api_view(["GET"])
def post_list(
    request: HttpRequest,
) -> Response:
    """Post list view."""
    posts = Post.objects.all()
    serializer = PostSerializer(
        posts,
        many=True,
        context={"request": request},
    )
    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )
