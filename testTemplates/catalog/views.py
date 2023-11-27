from django.shortcuts import render
from .models import Product

MENU = {"главная":"/", "статья":"/state", "о нас":"/about"}

def state_page(request):
    products = Product.objects.all()
    title = "Статья"
    data = {"menu":MENU, "title": title, "products": products}
    return render(request,"./state.html", context=data)