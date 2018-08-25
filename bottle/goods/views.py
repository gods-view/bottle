from django.shortcuts import render
from goods.models import Products


# Create your views here.
def index(request, type_good):
    # print(type_good)
    products = Products.objects.get(category=type_good)
    all_products = Products.objects.all()
    return render(request, "glassware.html", {"products": products, "all_products": all_products})


def mobile_index(request, type_good):
    # print(type_good)
    products = Products.objects.get(category=type_good)
    all_products = Products.objects.all()
    return render(request, "glasswareMobile.html", {"products": products, "all_products": all_products})
