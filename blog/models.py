from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30, verbose_name="Ім'я")
    bio = models.TextField(verbose_name="Біографія")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назві")
    content = models.TextField(verbose_name="Котент посту")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публікації")
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Автор"
    )

    def __str__(self):
        author_name = self.author.name if self.author else "невідомий"
        return f"{self.title} (Автор: {author_name})"

    def published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days=7)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"
        ordering = ["-published_date"]

class Comment(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Пост"
    )
    author_name = models.CharField(max_length=30, verbose_name="Ім'я автора")
    text = models.TextField(verbose_name="Текст коментаря")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата створення")

    def __str__(self):
        return f"{self.author_name} - {self.post.title}"

