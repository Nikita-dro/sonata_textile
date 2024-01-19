from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect, render  # NOQA: F401
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


class UserLogin(TemplateView):
    template_name = "registration/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        email_error = None
        password_error = None
        error = None
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            if not email and not password:
                password_error = "Введіть пароль"
                email_error = "Введіть електронну пошту"
            elif not email:
                email_error = "Введіть електронну пошту"
            elif not password:
                password_error = "Введіть пароль"
            else:
                error = "Ви ввели неправильні дані! Повторіть спробу знову"

        return render(
            request,
            self.template_name,
            {
                "email": email,
                "password": password,
                "email_error": email_error,
                "password_error": password_error,
                "error": error,
            },
        )


class UserLogout(LogoutView):
    ...


class ContactsView(TemplateView):
    template_name = "company/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class PartnersView(TemplateView):
    template_name = "company/partners.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
