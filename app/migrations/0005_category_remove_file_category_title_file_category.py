# Generated by Django 5.1.3 on 2024-11-20 22:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_file_category_title_alter_file_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название категории')),
            ],
        ),
        migrations.RemoveField(
            model_name='file',
            name='category_title',
        ),
        migrations.AddField(
            model_name='file',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='app.category', verbose_name='Категория'),
        ),
    ]
