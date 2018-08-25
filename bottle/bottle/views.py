from django.shortcuts import render
from goods.models import Products


def main(request):
    products = Products.objects.all()
    for item in products:
        print(item.category)
    return render(request, "home.html", {"products": products})


def mobile(request):
    products = Products.objects.all()
    for item in products:
        print(item.category)
    return render(request, "mobile.html", {"products": products})
