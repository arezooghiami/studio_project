from django.shortcuts import render
from .models import *


# Create your views here.
def product(request):
    category = Category.objects.all()
    return render(request, 'product/product.html', {'category': category})


def all_product(request, slug=None, id=None):
    products = Product.objects.all()
    category = Category.objects.all()
    if slug and id:
        data = Category.objects.get(slug=slug, id=id)
        products = products.filter(category=data)

    return render(request, 'product/all_product.html', {'products': products, 'category': category})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        variant = Variatns.objects.filter(product_variant_id=id)
        var_id = request.POST.get('select')
        variants = Variatns.objects.get(id=var_id)
        context = {
            'product': product,
            'variant': variant,
            'variants': variants,

        }


    else:
        variant = Variatns.objects.filter(product_variant_id=id)
        variants = Variatns.objects.get(id=variant[0].id)
        context = {
            'product': product,
            'variant': variant,
            'variants': variants,

        }

    return render(request, 'product/detail.html', context)
