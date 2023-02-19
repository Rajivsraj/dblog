from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password   # for password Hashing
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from django.views import View


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


class Signup(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        # Register User
        post_data = request.POST
        fname = post_data.get("fname")
        lname = post_data.get("lname")
        phone = post_data.get("phone")
        email = post_data.get("email")
        password = post_data.get("password")
        cus_obj = Customer(first_name=fname, last_name=lname, phone=phone, email=email, password=password)

        print("---------")
        # Validation
        err_msg = None

        values = {
            "first_name": fname,
            "last_name": lname,
            "phone": phone,
            "email": email,
            "password": password
        }

        if not fname:
            err_msg = "First Name Required"
        elif len(fname) < 2:
            err_msg = "First Name must be >=2 Charcaters"
        elif not lname:
            err_msg = "Last Name Required"
        elif len(lname) < 2:
            err_msg = "Last Name must be >=2 Character"
        elif not phone:
            err_msg = "Phone no. Required"
        elif len(phone) != 10:
            err_msg = "Phone no. leng must be 10 Digits"
        elif not email:
            err_msg = "Email Required"
        elif len(email) < 5:
            err_msg = "Email Must be >=5 characters"
        elif not password:
            err_msg = "Password Required"
        elif len(password) < 8:
            err_msg = f"Password Length must be >=8 {len(password)}"
        elif cus_obj.is_email_exists():
            err_msg = "Email Already Exists"

        if not err_msg:
            cus_obj.password = make_password(password)
            x = cus_obj.save()  # Save customer data
            return redirect("homepage")
        else:
            data = {
                "error_msg": err_msg,
                "all_values": values
            }
            return render(request, "signup.html", data)


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        customer = Customer.get_customer_by_email(email)
        err_msg = None

        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return redirect("homepage")
            else:
                err_msg = "Email or Password Invalid"
        else:
            err_msg = "Email or Password Invalid"
        print(customer, password)
        return render(request, "login.html", {"error_msg": err_msg})



"""
def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    else:
        # Register User
        post_data = request.POST
        fname = post_data.get("fname")
        lname = post_data.get("lname")
        phone = post_data.get("phone")
        email = post_data.get("email")
        password = post_data.get("password")
        cus_obj = Customer(first_name=fname, last_name=lname, phone=phone, email=email, password=password)

        print("---------")
        # Validation
        err_msg = None

        values = {
            "first_name": fname,
            "last_name": lname,
            "phone": phone,
            "email": email,
            "password": password
        }

        if not fname:
            err_msg = "First Name Required"
        elif len(fname) < 2:
            err_msg = "First Name must be >=2 Charcaters"
        elif not lname:
            err_msg = "Last Name Required"
        elif len(lname) < 2:
            err_msg = "Last Name must be >=2 Character"
        elif not phone:
            err_msg = "Phone no. Required"
        elif len(phone) != 10:
            err_msg = "Phone no. leng must be 10 Digits"
        elif not email:
            err_msg = "Email Required"
        elif len(email) < 5:
            err_msg = "Email Must be >=5 characters"
        elif not password:
            err_msg = "Password Required"
        elif len(password) < 8:
            err_msg = f"Password Length must be >=8 {len(password)}"
        elif cus_obj.is_email_exists():
            err_msg = "Email Already Exists"

        if not err_msg:
            cus_obj.password = make_password(password)
            x = cus_obj.save()  # Save customer data
            return redirect("homepage")
        else:
            data = {
                "error_msg": err_msg,
                "all_values": values
            }
            return render(request, "signup.html", data)
"""


# Login Function Based
"""def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        email = request.POST.get("email")
        password = request.POST.get("password")
        customer = Customer.get_customer_by_email(email)
        err_msg = None

        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return redirect("homepage")
            else:
                err_msg = "Email or Password Invalid"
        else:
            err_msg = "Email or Password Invalid"
        print(customer, password)
        return render(request, "login.html", {"error_msg": err_msg})"""