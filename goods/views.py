from django.shortcuts import render

# Контролер для каталога
def catalog(request):
    return render(request, 'goods/catalog.html')

# Отображение конктретного товара
def product(request):
    return render(request, 'goods/product.html')