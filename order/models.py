from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

from item.models import Item


class BillingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=200, null=True, choices=CountryField().choices + [('', 'Select Country')])
    street_address = models.CharField(max_length=200)
    apartment_address = models.CharField(max_length=200)


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} {self.timestamp}'


class OrderDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderDetails)
    order_date = models.DateTimeField(auto_now_add=True)
    shipping_address = models.ForeignKey(BillingAddress, related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(BillingAddress, related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} on {self.order_date}'

    def get_total(self):
        total = 0
        for item in self.items.all():
            total += item.price
        return total
