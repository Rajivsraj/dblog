from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category

# Create your views here.
def index(request):
    products = Product.get_all_products()
    categories = Category.get_all_categories()
    data = {
        "all_products": products,
        "all_categories": categories
    }
    print(products)
    return render(request, "index.html", data)