from django.shortcuts import render
from .models import Product, ProductComment

MENU = {"главная":"/", "статья":"/state", "о нас":"/about", "отзывы":"/state/add_comment"}

def state_page(request):
    products = Product.objects.all()
    title = "Статья"
    data = {"menu":MENU, "title": title, "products": products}
    return render(request,"./state.html", context=data)

def add_comment_page(request):
    products = Product.objects.values("id", "name")
    title = "Добавить комментарий"
    add_comments = ProductComment.objects.filter(checked=True).order_by('-id')
    data = {"menu":MENU, "title": title, "products": products, "add_comments":add_comments}
    return render(request,"./add_comment.html", context=data)

def thaks_page(request):
    user_name = request.POST['user_name']
    comment = request.POST['comment']
    email = request.POST['email']
    product = Product.objects.get(pk=request.POST['product'])
    ProductComment.objects.create(user_name=user_name, comment=comment, product=product, email=email)
    title = "Страница благодарности"
    data = {"menu":MENU, "title": title, "user_name":user_name}
    return render(request,"./thaks.html", context=data)



