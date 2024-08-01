from django.db import models
from common.models import CommonModel
from users.models import User
from django.utils.timezone import now


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
    views = models.PositiveIntegerField(
        default=0,
        verbose_name="조회수",
    )
    is_modified = models.BooleanField(default=False)
    modified_at = models.DateTimeField(default=now)
    likes = models.ManyToManyField(
        User,
        related_name="liked_posts",
        verbose_name="좋아요",
    )
    dislikes = models.ManyToManyField(
        User,
        related_name="disliked_posts",
        verbose_name="싫어요",
    )

    def __str__(self) -> str:
        return self.title

    def is_like(self, user):
        return self.likes.filter(id=user.id).exists()

    def add_like(self, user):
        self.likes.add(user)
        self.save()

    def remove_like(self, user):
        self.likes.remove(user)
        self.save()

    def is_dislike(self, user):
        return self.dislikes.filter(id=user.id).exists()

    def add_dislike(self, user):
        self.dislikes.add(user)
        self.save()

    def remove_dislike(self, user):
        self.dislikes.remove(user)
        self.save()


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
