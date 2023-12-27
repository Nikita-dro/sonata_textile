from django.shortcuts import render  # NOQA: F401
from django.views.generic import ListView, TemplateView

from products.models import Category, Product


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["products"] = Product.objects.filter(hit_sale=True)
        return context


class AboutUsView(TemplateView):
    template_name = "company/about_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class AllCategoriesView(ListView):
    model = Category
    template_name = "category/index_category.html"
    context_object_name = "categories"


class DeliveryView(TemplateView):
    template_name = "company/delivery.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
