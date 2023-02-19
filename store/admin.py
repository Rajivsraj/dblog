from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

# Register your models here.

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ["name", "price", "category"]


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Customer)
class AdminCustomer(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone", "email", "password"]

