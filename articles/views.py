from django.shortcuts import render
from django.core.cache import cache
from catalog.models import Category
from .models import Article


def article_page(request):
    categories = cache.get_or_set('categories', Category.objects.all())
    sorted_article_list = Article.objects.all().filter(is_active=True)
    return render(request, 'main_page.html', {
        'categories': categories,
        'articles': sorted_article_list
    })
