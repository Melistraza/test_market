from django import forms
from product.models import Comment


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', ]
