from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_email', 'created', 'display_num_orders', 'status',]
    list_editable = ['status']
    list_filter = ['id', 'created']
    fields = ('user', 'first_name', 'last_name', 'user_email', 'status',)
    readonly_fields = ('user_email', 'first_name', 'last_name')

    def email_from_admin(self, obj):
        return obj.user.email

    def first_name(self, obj):
        if obj.user.first_name:
            return obj.user.first_name
        else:
            return 'Не указано'

    def last_name(self, obj):
        if obj.user.last_name:
            return obj.user.last_name
        else:
            return 'Не указано'

    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
