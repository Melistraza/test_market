from django import forms
from apps.product.models import Comment


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', ]

    def clean_text(self):
        data = self.cleaned_data['text']
        if len(data) <= 4:
            raise forms.ValidationError(
                "Put a little more about their impressions about the product!")
        return data
