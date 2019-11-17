from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Product, Category
from .cart import Cart
from django.core.cache import cache


def cart_detail(request):
    cart = Cart(request)
    quantity = len(request.session.get('cart'))
    categories = cache.get_or_set('categories', Category.objects.all())
    return render(request, 'cart.html',
                  {'cart': cart,
                   'quantity': quantity,
                   'categories': categories
                   })

@require_POST
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=id)
    cart.add_product(product=product)
    referer = request.META.get('HTTP_REFERER', None)
    if referer:
        return HttpResponseRedirect(referer)
    else:
        return redirect('index')


def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=id)
    cart.remove(product)
    return redirect('cart:main')
