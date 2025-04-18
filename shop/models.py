from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.name


class Customer(models.Model):  #Customer = مشتری
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    class Meta:
        verbose_name = " مشتری"
        verbose_name_plural = " مشتری ها"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Profile(models.Model):
    user = models.OneToOneField( User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User,auto_now=True)
    phone = models.CharField(max_length=250, blank=True)
    address1 = models.CharField(max_length=250, blank=True)
    address2 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=25, blank=True)
    stat = models.CharField(max_length=25, blank=True)
    zipcode = models.CharField(max_length=25, blank=True)
    country = models.CharField(max_length=25, default='IRAN')
    old_cart = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = " پروفایل"
        verbose_name_plural = " پروفایل ها"

    def __str__(self):
        return self.user.username
    
def create_profile(sender, instance , created, **kwargs):
    if created:
        user_profile = Profile(user = instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)


class Product(models.Model): # Product = محصول
    name = models.CharField(max_length=40)
    description =models.CharField(max_length=500, default='', blank=True, null=True)    #description = توضیحات
    price = models.DecimalField(default=0, decimal_places=0,max_digits=12)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    picture = models.ImageField(upload_to='upload/product/')
    star = models.IntegerField(default=0 , validators=[MinValueValidator(0) , MaxValueValidator(5)] )
    is_sale = models.BooleanField(default=False)  # is_sale = تخفیف ویژه
    sale_price = models.DecimalField(default=0, decimal_places=0,max_digits=12)   # sale_price = قیمت ویژه

    class Meta:
        verbose_name = " محصول"
        verbose_name_plural = " محصولات"

    def __str__(self):
        return self.name


class Order(models.Model):   # Order = سفارشات
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1) #quantity = تعداد
    address = models.CharField(max_length=400,default='',blank=False)
    phone = models.CharField(max_length=20,blank=True)
    date = models.DateField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = " سفارش"
        verbose_name_plural = " سفارشات"

    def __str__(self):
        return self.product
