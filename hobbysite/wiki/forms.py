from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['author']
        fields = '__all__'
        labels = {
            'title': 'Article name',
            'entry': '',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Entry Title...'}),
            'entry': forms.Textarea(attrs={'placeholder': 'Entry Text...'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Choose a category:'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']
        labels = {
            'entry': '',
        }
        widgets = {
            'entry': forms.Textarea(attrs={'placeholder': 'Write a comment...'}),
        }