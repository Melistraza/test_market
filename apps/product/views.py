from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from apps.product.models import Product, Comment
from apps.product.forms import CommentsForm
last_day = datetime.now() - timedelta(days=1)


def product_list(request):
    '''
    Show list of all product, separate it for page, 10 product in page
    '''

    sort = request.GET.get('sort')
    # by the end of the job is already lazy
    if sort == 'like':
        product_list = Product.objects.all().order_by('-likes')
    else:
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
    product = get_object_or_404(Product, slug=product_slug)
    comments = Comment.objects.filter(
        product=product, created_at__gt=last_day).order_by('-created_at')[:10]
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
            # return success message & redirect to product page
            messages.success(request, 'Thanks for comment!')
            return redirect(
                reverse('product_page', kwargs={'product_slug': product.slug}))

    else:
        form = CommentsForm()
    return render(request, 'product/product.html',
                  {'product': product, 'form': form, 'comments': comments})


@login_required
def like(request, product_slug):
    '''
    Liker for product. One user can like one product once.

    likes work without ajax, because the requirement in the task to use
    messages easy to change just need add if request.is_ajax() after
    if request.method == 'POST in product_page view and change return

    for manual you can use
    stackoverflow.com/questions/14007453/my-own-like-button-django-ajax-how
    '''
    user = request.user
    product = get_object_or_404(Product, slug=product_slug)
    if product.likes.filter(id=user.id).exists():
        # user has already liked this product
        # remove like/user
        product.likes.remove(user)
        messages.success(request, 'You disliked this')
    else:
        # add a new like for a product
        product.likes.add(user)
        messages.success(request, 'You liked this')
    return redirect(reverse('product_page',
                            kwargs={'product_slug': product.slug}))
