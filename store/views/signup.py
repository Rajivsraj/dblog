from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password   # for password Hashing
from store.models.customer import Customer
from django.views import View


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