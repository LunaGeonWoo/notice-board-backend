from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Reply
from .serializers import ReplySerializer


class ReplyListCreateAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, comment_id):
        replies = Reply.objects.filter(comment_id=comment_id)
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)

    def post(self, request, comment_id):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(comment_id=comment_id, writer=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReplyDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Reply.objects.get(id=id)
        except Reply.DoesNotExist:
            raise exceptions.NotFound

    def put(self, request, id):
        reply = self.get_object(id)
        if reply.writer != request.user:
            raise exceptions.PermissionDenied
        serializer = ReplySerializer(reply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        reply = self.get_object(id)
        if reply.writer != request.user:
            raise exceptions.PermissionDenied
        reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
