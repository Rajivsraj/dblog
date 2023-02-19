from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password   # for password Hashing
from store.models.customer import Customer
from django.views import View


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