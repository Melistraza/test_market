from django import forms
from apps.product.models import Comment


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', ]
