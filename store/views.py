from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category


# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_categories()

    category_id = request.GET.get("cat_id")

    if category_id:
        products = Product.get_all_products_by_cat_id(category_id)
    else:
        products = Product.get_all_products()

    data = {
        "all_products": products,
        "all_categories": categories
    }

    return render(request, "index.html", data)