from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
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

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise exceptions.NotFound

    def get(self, request, pk):
        post = self.get_object(pk)
        Post.objects.filter(pk=pk).update(views=F("views") + 1)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk=pk)
        if post.writer != request.user:
            raise exceptions.PermissionDenied
        serializer = PostCreateSerializer(post, data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            serializer = PostDetailSerializer(post)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        if post.writer != request.user:
            raise exceptions.PermissionDenied
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostLikeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise exceptions.NotFound

    def post(self, request, pk):
        post = self.get_object(pk=pk)
        if post.is_like(request.user):
            return Response({"detail": "Already liked."})

        if post.is_dislike(request.user):
            post.remove_dislike(request.user)
        post.add_like(request.user)
        return Response({"detail": "Liked."})

    def delete(self, request, pk):
        post = self.get_object(pk=pk)
        if post.is_like(request.user):
            post.remove_like(request.user)
            return Response({"detail": "Like removed."})
        else:
            return Response({"detail": "You have not liked this post."})


class PostDislikeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise exceptions.NotFound

    def post(self, request, pk):
        post = self.get_object(pk=pk)
        if post.is_dislike(request.user):
            return Response({"detail": "Already disliked."})

        if post.is_like(request.user):
            post.remove_like(request.user)
        post.add_dislike(request.user)
        return Response({"detail": "Disliked."})

    def delete(self, request, pk):
        post = self.get_object(pk=pk)
        if post.is_dislike(request.user):
            post.remove_dislike(request.user)
            return Response({"detail": "Dislike removed."})
        else:
            return Response({"detail": "You have not disliked this post."})
