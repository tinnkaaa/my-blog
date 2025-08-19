from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назві")
    content = models.TextField(verbose_name="Котент посту")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публікації")

    def __str__(self):
        return self.title



