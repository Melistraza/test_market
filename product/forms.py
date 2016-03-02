from django import forms
from product.models import Comment


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]
    #
    # def clean_user(self, request):
    #     if request.user.is_authenticated():
    #         return User.objects.get(email=request.user.email)
    #     else:
    #         return None
    #
    # def clean_product(self):
    #     product_slug = self.cleaned_data['product']
    #     try:
    #         return Product.objects.get(slug=product_slug)
    #     except ObjectDoesNotExist:
    #         return None
