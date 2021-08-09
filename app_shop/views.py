from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView
from app_shop.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(ListView):
    model = Product
    template_name = "app_shop/Home.html"
class ProductDetail(LoginRequiredMixin,DetailView):
    model = Product
    template_name = "app_shop/product_detail.html"
