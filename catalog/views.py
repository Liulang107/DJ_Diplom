from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Review
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ReviewForm
from django.core.cache import cache


def product_list(request, category_slug):
    categories = cache.get_or_set('categories', Category.objects.all())
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    paginator = Paginator(products, 3)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request,
                  'product_list.html',
                  {'category': category.name,
                   'categories': categories,
                   'product_list': products,
                   })


def product_detail(request, id, category_slug):
    product = get_object_or_404(Product, pk=id)
    categories = cache.get_or_set('categories', Category.objects.all())

    context = {'categories': categories,
               'category': product.category.name,
               'product': product
               }

    if request.POST:
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(product=product,
                                  author=form.cleaned_data['name'],
                                  text=form.cleaned_data['description'],
                                  rate=form.cleaned_data['radio_mark'])
            return redirect(product.get_absolute_url())
    else:
        context['form'] = ReviewForm()

    context['reviews'] = Review.objects.filter(product=product).order_by('created')
    return render(request, 'product_detail.html', context)
