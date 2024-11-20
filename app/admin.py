from django.contrib import admin
from .models import Category, File

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass
