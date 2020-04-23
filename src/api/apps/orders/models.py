from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from decimal import Decimal
from django.db.models import Sum
from api.apps.products.models import Product


class Order(models.Model):
    customer = models.ForeignKey(
        get_user_model(), blank=True, on_delete=models.CASCADE)
    total_price = models.IntegerField(default=0)
    products = models.ManyToManyField(
        Product, through="ProductinOrder", related_name="orders")

    def __str__(self):
        return f'{self.customer} {self.total_price} {self.products}'

    # def get_order_products(self):
    #     order_products = self.products.all()
    #     if order_products.exists():
    #         for product in order_products:
    #             total_price += product.unit_price

    #     return total_price


class ProductinOrder(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, default=0)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=0)
    total_price = models.IntegerField(default=0)
    quantity = models.IntegerField(
        default=1)

    def __str__(self):
        return f'{self.product.description}'

    def save(self,  *args, **kwargs):
        self.total_price = self.quantity * \
            self.product.unit_price
        super().save(*args, **kwargs)
        self.order.total_price += self.total_price
        self.order.save()


# >> > p = Product.objects.create(name='iPhone7', description='The best phone on the market', unit_price=45000, quantity=10)
# >> > p.save()
# >> > o = Order.objects.create(customer=User.objects.create(username='Mutuba', email='d@gmail.com', password='baraka12'))
# >> > o.save()
# >> > o
# <Order: Order object(1) >
# >> > o.customer
# <User: Mutuba >
# >> > po = ProductinOrder.objects.create(product=p, order=o, quantity=2)
