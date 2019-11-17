from django.contrib import admin
from .models import Article, ArticleItem


class ArticleItemInline(admin.TabularInline):
    model = ArticleItem
    raw_id_fields = ['product']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'is_active']
    list_filter = ['id', 'is_active']
    list_editable = ['is_active']
    inlines = [ArticleItemInline]


admin.site.register(Article, ArticleAdmin)
