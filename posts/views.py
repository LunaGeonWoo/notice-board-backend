from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Post
from .serializers import PostListSerializer, PostCreateSerializer, PostDetailSerializer


class PostListCreateAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(writer=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise exceptions.NotFound

    def get(self, request, id):
        post = Post.objects.get(id=id)
        post.views += 1
        post.save()
        serializer = PostDetailSerializer(post, context={"request": request})
        return Response(serializer.data)

    def put(self, request, id):
        post = self.get_object(id)
        if post.writer != request.user:
            raise exceptions.PermissionDenied
        serializer = PostCreateSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        post = self.get_object(id)
        if post.writer != request.user:
            raise exceptions.PermissionDenied
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
