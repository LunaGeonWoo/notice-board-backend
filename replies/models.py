from django.db import models
from comments.models import Comment
from users.models import User
from common.models import CommonModel


class Reply(CommonModel):
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="replies",
    )
    writer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="작성자",
    )
    detail = models.TextField()
    is_modified = models.BooleanField(
        default=False,
        editable=False,
    )

    def __str__(self) -> str:
        return f"{self.comment}/{self.writer}의 답글"

    class Meta:
        verbose_name = "reply"
        verbose_name_plural = "replies"
