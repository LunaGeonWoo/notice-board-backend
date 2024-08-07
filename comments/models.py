from django.db import models
from common.models import CommonModel
from posts.models import Post
from users.models import User


class Comment(CommonModel):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    detail = models.TextField()
    writer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="작성자",
    )
    is_modified = models.BooleanField(
        default=False,
        editable=False,
    )

    def __str__(self) -> str:
        return f"{self.post}/{self.writer}의 댓글"
