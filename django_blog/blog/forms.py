from django import forms
from .models import Post
from django import forms
from .models import Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
        'title': forms.TextInput(attrs={'placeholder': 'Post title', 'class': 'form-control'}),
        'content': forms.Textarea(attrs={'placeholder': 'Write your post here...', 'class': 'form-control', 'rows': 8}),
        }
        tags_field = forms.CharField(
        required=False,
        label='Tags',
        help_text='Comma-separated. Example: django, tips, deployment'
    )

    def clean_title(self):
        title = self.cleaned_data.get('title', '')
        if not title.strip():
            raise forms.ValidationError('Title cannot be empty or only whitespace.')
        return title
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write a thoughtful comment...'
            })
        }

    def clean_content(self):
        content = (self.cleaned_data.get('content') or '').strip()
        if not content:
            raise forms.ValidationError('Comment cannot be empty.')
        if len(content) > 20000:
            raise forms.ValidationError('Comment too long.')
        return content
