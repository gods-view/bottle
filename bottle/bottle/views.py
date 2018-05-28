from django.shortcuts import render
from goods.models import Products


def main(request):
    products = Products.objects.all()
    return render(request, "home.html", {"products": products})
