from django.db import models
from common.models import CommonModel
from users.models import User


class Post(CommonModel):
    title = models.CharField(
        max_length=100,
        verbose_name="제목",
    )
    detail = models.TextField()
    writer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="작성자",
    )
    like = models.PositiveIntegerField(
        default=0,
        verbose_name="좋아요",
    )
    dislike = models.PositiveIntegerField(
        default=0,
        verbose_name="싫어요",
    )

    def __str__(self) -> str:
        return self.title


class Comment(CommonModel):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    detail = models.TextField()
    writer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="작성자",
    )

    def __str__(self) -> str:
        return f"{self.post}/{self.writer}의 댓글"


class Reply(CommonModel):
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        verbose_name="답글",
    )
    writer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="작성자",
    )
    detail = models.TextField()

    def __str__(self) -> str:
        return f"{self.comment}/{self.writer}의 답글"

    class Meta:
        verbose_name = "reply"
        verbose_name_plural = "replies"