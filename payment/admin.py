from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem


class OrderItemAdmin(admin.ModelAdmin):
    list_display=["order","product","quantity","price"]


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display=["user","shipping_full_name","shipping_email","shipping_zipcode"]



# Register your models here.
admin.site.register(ShippingAddress,ShippingAddressAdmin)
#admin.site.register(Order)
admin.site.register(OrderItem,OrderItemAdmin)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['date_ordered', 'last_update']
    inlines = [OrderItemInline]