from django import forms
from blog.models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='', 
        required=True, 
        widget=forms.TextInput(
            attrs={
                "placeholder": "Post Title", 
                "class": "form-control"
            }
        )
    )

    body = forms.CharField(
        label='', 
        required=True, 
        widget=forms.Textarea(
            attrs={
                "placeholder": "Post Body Content", 
                "class": "form-control", 
                "id": "bodyTextArea", 
                "rows": "15"
            }
        )
    )
    
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
        ]