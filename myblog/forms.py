from django import forms
from .models import Post, Category

#choices=[('Football','Football'),('Coding','Coding'),('Manga','Manga')]
choices = Category.objects.all().values_list('name','name')
choice_list= []
for item in choices:
    choice_list.append(item)


class Post_form(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('title', 'title_tag', 'author','category','body','snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'title_tag': forms.TextInput(attrs={'class': "form-control"}),
            'author': forms.Select(attrs={'class': "form-control"}),
            'category':forms.Select(choices= choice_list, attrs={'class': "form-control"}),
            'body': forms.Textarea(attrs={'class': "form-control"}),
            'snippet':forms.Textarea(attrs={'class': "form-control"}),
        }


class Edit_form(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('title', 'title_tag', 'body','snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'title_tag': forms.TextInput(attrs={'class': "form-control"}),
            #'author': forms.Select(attrs={'class': "form-control"}),
            'body': forms.Textarea(attrs={'class': "form-control"}),
            'snippet': forms.Textarea(attrs={'class': "form-control"}),
            
        }