from django import forms 
from .models import File, Category


class FileUploadForm(forms.Form):
    file = forms.FileField(required=True)
    category = forms.CharField(required=False)

    def save(self):
        instance = File()
        instance.file = self.cleaned_data['file']
        category_title = self.cleaned_data['category']
        if category_title:
            instance.category, created = Category.objects.get_or_create(title=category_title)
        
        instance.save()
        return instance

