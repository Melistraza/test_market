from django.shortcuts import render, redirect
from apps.shop.models import Product, Comment
from apps.shop.forms import CommentsForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from datetime import datetime, timedelta
last_day = datetime.now() - timedelta(days=1)


def product_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 10)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'shop/product_list.html', {'products': products})


def product_page(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    comments = Comment.objects.filter(product=product, created_at__gt=last_day).order_by('-created_at')[:10]
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            # validate form in view in this case, much faster
            try:
                product = Product.objects.get(slug=product_slug)
            except ObjectDoesNotExist:
                product = None

            if request.user.is_authenticated():
                user = User.objects.get(email=request.user.email)
            else:
                user = None
            text = form.cleaned_data['text']
            Comment.objects.create(product=product, user=user, text=text)
            messages.success(request, 'Thanks for comment!')
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = CommentsForm()
    return render(request, 'shop/product.html', {'product': product, 'form': form, 'comments': comments})

