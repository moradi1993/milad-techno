from django.contrib import admin
from . import models
from django.contrib.auth.models import User


class ProfileAdmin(admin.ModelAdmin):
    list_display=["user","date_modified","city","stat","old_cart"]

class ProductAdmin(admin.ModelAdmin):
    list_display=["name","category","price","is_sale"]

class CategoryAdmin(admin.ModelAdmin):
    list_display=["id","name"]

# Register your models here.
admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Customer)
admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.Order)
admin.site.register(models.Profile,ProfileAdmin)



class ProfileInline(admin.StackedInline):
    model = models.Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username','first_name','last_name','email']
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
