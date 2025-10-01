from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
        'title': forms.TextInput(attrs={'placeholder': 'Post title', 'class': 'form-control'}),
        'content': forms.Textarea(attrs={'placeholder': 'Write your post here...', 'class': 'form-control', 'rows': 8}),
        }


    def clean_title(self):
        title = self.cleaned_data.get('title', '')
        if not title.strip():
            raise forms.ValidationError('Title cannot be empty or only whitespace.')
        return title