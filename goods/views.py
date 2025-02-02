from typing import Any
from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.db.models.base import Model as Model
from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView

from goods.models import Products
from goods.utils import q_search

# Контролер для каталога
def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Products.objects.filter(category__slug=category_slug)
        if not goods.exists():
            raise Http404()

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    # Вывод 3х товаров
    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context= {
        "title": "Home - Каталог",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


# Отображение конктретного товара
class ProductView(DetailView):
    # model = Products
    # slug_field = "slug"
    template_name = "goods/product.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"

    def get_object(self, queryset=None):
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context

# def product(request, product_slug):

#     product = Products.objects.get(slug=product_slug)

#     context = {
#         'product': product,
#     }

#     return render(request, "goods/product.html", context)
