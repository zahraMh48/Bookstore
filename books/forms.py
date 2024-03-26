from django import forms

from .models import Comment


# we want to show the comment form and submit it
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text','recomend',)