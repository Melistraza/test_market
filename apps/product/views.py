from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from apps.product.models import Product, Comment
from apps.product.forms import CommentsForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

last_day = datetime.now() - timedelta(days=1)


def product_list(request):
    '''
    Show list of all product, separate it for page, 10 product in page
    '''
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 10)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'product/product_list.html', {'products': products})


def product_page(request, product_slug):
    '''
    Personal page for product.
    '''
    product = Product.objects.get(slug=product_slug)
    comments = Comment.objects.filter(
        product=product, created_at__gt=last_day).order_by('-created_at')[:10]
    # likes = Like.objects.filter(product=product)
    if request.method == 'POST':
        # post form for comment
        form = CommentsForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            if request.user.is_authenticated():
                user = request.user
            else:
                user = None
            Comment.objects.create(product=product, user=user, text=text)
            # return success message
            messages.success(request, 'Thanks for comment!')
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = CommentsForm()
    return render(request, 'product/product.html',
                  {'product': product, 'form': form, 'comments': comments})
