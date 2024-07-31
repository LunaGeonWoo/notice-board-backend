from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostListSerializer
from .models import Post


class PostListAPIView(APIView):

    def get(self, request):
        post = Post.objects.all()
        serializer = PostListSerializer(post, many=True)
        return Response(serializer.data)
