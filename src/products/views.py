from django.db.models import Q
from django.shortcuts import render  # NOQA: F401
from django.views.generic import DetailView, ListView, TemplateView

from products.models import Category, Material, Product


class ProductListView(TemplateView):
    model = Category
    template_name = "category/products.html"

    def get(self, request, *args, **kwargs):
        material_filter = request.GET.get("material")
        price_filter = request.GET.get("price")
        category = self.model.objects.get(pk=self.kwargs["pk"])
        if material_filter and price_filter:
            if price_filter == "0":
                products = Product.objects.filter(Q(category=category) & Q(material__pk=material_filter)).order_by(
                    "-price"
                )
            else:
                products = Product.objects.filter(Q(category=category) & Q(material__pk=material_filter)).order_by(
                    "price"
                )
        elif material_filter:
            products = Product.objects.filter(Q(category=category) & Q(material__pk=material_filter))
        elif price_filter:
            if price_filter == "0":
                products = Product.objects.filter(category=category).order_by("-price")
            else:
                products = Product.objects.filter(category=category).order_by("price")
        else:
            products = Product.objects.filter(category=category)
        context = {
            "products": products,
            "materials": Material.objects.all(),
            "categories": Category.objects.all(),
            "material_filter": material_filter,
            "price_filter": price_filter,
            "category": category,
        }
        if material_filter:
            context["material"] = Material.objects.get(id=material_filter)
        return render(request, self.template_name, context)


class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product_info.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["products"] = Product.objects.filter(hit_sale=True)
        return context


class ProductSearchListView(ListView):
    model = Product
    template_name = "product/search_product.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_text = self.request.GET.get("search_text", "")

        if search_text:
            name_filter = Q(name__iregex=rf".*{search_text}.*")
            article_filter = Q(article__icontains=str(search_text))
            queryset = queryset.filter(name_filter | article_filter)

        return queryset
