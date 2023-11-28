from django.http import HttpResponse
from django.shortcuts import render



MENU = {"главная":"/", "статья":"/state", "о нас":"/about"}

def main_page(request):
    title = ""
    data = {"menu":MENU, "title": title}
    return render(request,"./index.html", context=data)

def about_page(request):
    title = "О нас"
    data = {"menu":MENU, "title": title}
    return render(request,"./about.html", context=data)

