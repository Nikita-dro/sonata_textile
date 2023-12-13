from django.shortcuts import render  # NOQA: F401
from django.views.generic import TemplateView

from products.models import Category, Product


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["products"] = Product.objects.filter(hit_sale=True)
        return context
