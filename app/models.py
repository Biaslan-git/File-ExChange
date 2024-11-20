from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="Название категории")

    def __str__(self):
        return self.title


class File(models.Model):
    file = models.FileField(upload_to='files', verbose_name='Ваш файл')
    category = models.ForeignKey(
        Category, 
        models.CASCADE, 
        related_name='files', 
        verbose_name='Категория',
        null=True,
        blank=True
    )

    @property
    def file_name(self):
        return self.file.name.split('/')[-1]  # Возвращает только имя файла

    def __str__(self):
        return self.file.name

