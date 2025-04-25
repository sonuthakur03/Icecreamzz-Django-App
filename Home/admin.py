from django.contrib import admin
from Home.models import Contact, CustomOrder, Order

# Register your models here.
admin.site.register(Contact)
admin.site.register(CustomOrder)
admin.site.register(Order)