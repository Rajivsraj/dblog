from django.contrib import admin
from django.urls import path
# from . import views
# from .views import home, login, signup # or
from .views.home import index
from .views.signup import Signup
from .views.login import Login

urlpatterns = [

    path("", index, name="homepage"),
    path("signup/", Signup.as_view(), name="signup"),
    path("login/", Login.as_view(), name="login"),

    # Function based URLS
    # path("signup/", views.signup),

]
