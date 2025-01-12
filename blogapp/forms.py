from django import forms
from .models import Blog, Loyiha
from django_quill.forms import QuillFormField  # QuillField o'rniga QuillFormField


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

class AddBlogForm(forms.ModelForm):
    content = QuillFormField()
    tags = forms.CharField(max_length=500)
    class Meta:
        model = Blog
       
        fields = ['title', 'content','image', 'category', 'tags']

class BlogUpdateForm(forms.ModelForm):
    tags = forms.CharField(max_length=500)
    class Meta:
        model = Blog
        fields = ['title','image','category']

class LoyihaForm(forms.ModelForm):
    class Meta:
        model = Loyiha 
        fields = ['name', 'image','text']       