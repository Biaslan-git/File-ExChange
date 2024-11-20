# Generated by Django 5.1.3 on 2024-11-20 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_file_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='category_title',
            field=models.CharField(default='Другие', max_length=100, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='files', verbose_name='Ваш файл'),
        ),
    ]