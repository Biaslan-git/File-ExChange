from django.urls import path
from .views import upload_file, files, main

urlpatterns = [
    path('', main, name='main'),
    path('upload/', upload_file, name='upload'),
    path('files/', files, name='files'),
]
