from django.shortcuts import render
from apps.shop.models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def product_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 10)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)
    return render(request, 'shop/product_list.html', {'products': products})
