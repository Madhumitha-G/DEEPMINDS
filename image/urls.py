from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path("",views.login,name="login"),
    path("base/", views.index, name="index"),
    path("register/", views.register, name="register"),
    # path("login/", views.login, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("search/",views.search,name="search"),

]