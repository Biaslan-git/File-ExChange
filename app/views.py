from django.http import FileResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import FileUploadForm
from .models import File, Category

def main(request):
    return redirect('files')

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            return render(request, 'app/upload.html', {'file': file})
    else:
        form = FileUploadForm()

    return render(request, 'app/upload.html', {'form': form})

def files(request):
    categories = Category.objects.all()
    other_files = File.objects.filter(category__isnull=True)
    context = {
        'categories': categories,
        'other_files': other_files,
    }
    return render(request, 'app/files_list.html', context)
