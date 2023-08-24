from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(orderItem)
admin.site.register(shipping)
admin.site.register(category) 