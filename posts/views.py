from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import (
    PostListSerializer,
    PostCreateSerializer,
    PostDetailSerializer,
    CommentSerializer,
    ReplySerializer,
)
from .models import Post, Comment, Reply


class PostListAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(writer=request.user)
            return Response(status=status.HTTP_201_CREATED)
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
        post.views += 1
        post.save()
        serializer = PostDetailSerializer(post, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk=pk)
        if post.writer != request.user:
            raise exceptions.PermissionDenied
        serializer = PostCreateSerializer(post, data=request.data)
        if serializer.is_valid():
            post = serializer.save(is_modified=True, modified_at=now())
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
            return Response(
                {"detail": "Already liked."}, status=status.HTTP_400_BAD_REQUEST
            )

        if post.is_dislike(request.user):
            post.remove_dislike(request.user)
        post.add_like(request.user)
        return Response({"detail": "Liked."}, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        post = self.get_object(pk=pk)
        if post.is_like(request.user):
            post.remove_like(request.user)
            return Response(
                {"detail": "Like removed."}, status=status.HTTP_204_NO_CONTENT
            )
        else:
            return Response(
                {"detail": "You have not liked this post."},
                status=status.HTTP_400_BAD_REQUEST,
            )


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
            return Response(
                {"detail": "Already disliked."}, status=status.HTTP_400_BAD_REQUEST
            )

        if post.is_like(request.user):
            post.remove_like(request.user)
        post.add_dislike(request.user)
        return Response({"detail": "Disliked."}, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        post = self.get_object(pk=pk)
        if post.is_dislike(request.user):
            post.remove_dislike(request.user)
            return Response(
                {"detail": "Dislike removed."}, status=status.HTTP_204_NO_CONTENT
            )
        else:
            return Response(
                {"detail": "You have not disliked this post."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class CommentAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        comments = Comment.objects.filter(post_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post_id=pk, writer=request.user)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentModifyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise exceptions.NotFound

    def put(self, request, pk, comment_pk):
        comment = self.get_object(comment_pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReplyAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk, comment_pk):
        replies = Reply.objects.filter(comment_id=comment_pk)
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)

    def post(self, request, pk, comment_pk):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(comment_id=comment_pk, writer=request.user)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReplyModifyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Reply.objects.get(pk=pk)
        except Reply.DoesNotExist:
            raise exceptions.NotFound

    def put(self, request, pk, comment_pk, reply_pk):
        reply = self.get_object(reply_pk)
        serializer = ReplySerializer(reply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
