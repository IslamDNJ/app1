from django.shortcuts import render

from goods.models import Products

# Контролер для каталога
def catalog(request):

    goods = Products.objects.all()

    context= {
        "title": "Home - Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


# Отображение конктретного товара
def product(request, product_id):
    
    product = Products.objects.get(id=product_id)
    context = {
        'product': product,
    }

    return render(request, "goods/product.html", context=context)
