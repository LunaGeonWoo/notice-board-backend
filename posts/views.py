from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostListSerializer, PostCreateSerializer, PostDetailSerializer
from .models import Post


class PostListAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        post = Post.objects.all()
        serializer = PostListSerializer(post, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save(writer=request.user)
            serializer = PostCreateSerializer(post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise exceptions.NotFound

    def get(self, request, id):
        post = self.get_object(id)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)
