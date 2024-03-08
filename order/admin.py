from django.contrib import admin

from .models import Order, OrderDetails, Payment, BillingAddress

admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(Payment)
admin.site.register(BillingAddress)