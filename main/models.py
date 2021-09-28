from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=40, verbose_name="Название")
    text = models.CharField(max_length=255, verbose_name="Текст")
    author = models.CharField(max_length=10, verbose_name="Автор", default="Anonymus")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"