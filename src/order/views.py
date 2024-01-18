import json

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render  # NOQA: F401
from django.views.generic import TemplateView

from config.settings.base import EMAIL_HOST_USER
from order.forms import OrderForm
from order.models import Cart, CartItem
from order.tasks import generate_cart
from products.models import Category, Product


def add_to_cart(request):
    return_dict = dict()
    data = request.POST
    product = get_object_or_404(Product, pk=data.get("product_id"))
    if data.get("update_quantity") and data.get("update_quantity") != "":
        quantity_action = data.get("update_quantity")
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(cart=cart, product=product)
        if quantity_action == "true":
            cart_item.quantity += 1
        elif quantity_action == "false":
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
        cart_item.save()
    elif data.get("basket") == "true":
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not item_created:
            cart_item.quantity += 1
        else:
            cart_item.quantity = 1

        cart_item.save()
    else:
        cart = Cart.objects.get(user=request.user)
        CartItem.objects.get(cart=cart, product=product).delete()
    products_number = CartItem.objects.filter(cart=cart)
    total = 0
    total_price = 0
    return_dict["products_list"] = list()

    for cart_item_obj in products_number:
        total += cart_item_obj.quantity
        total_price += cart_item_obj.quantity * cart_item_obj.product.price.amount
        product_dict = dict()
        product_dict["id_product"] = cart_item_obj.product.id
        product_dict["image_product"] = cart_item_obj.product.avatar.url
        product_dict["article"] = cart_item_obj.product.article
        product_dict["name_product"] = cart_item_obj.product.name
        product_dict["price_product"] = cart_item_obj.product.price.amount
        product_dict["quantity"] = cart_item_obj.quantity
        return_dict["products_list"].append(product_dict)

    return_dict["products_number"] = total
    return_dict["products_total_price"] = total_price
    return JsonResponse(return_dict)


class ShowBasketView(TemplateView):
    template_name = "orders/basket.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.get(user=self.request.user)
        products_cart = CartItem.objects.filter(cart=cart)
        context["categories"] = Category.objects.all()
        context["products_number"] = products_cart
        return context


def cart_generate(request):
    users = get_user_model().objects.all()
    products = Product.objects.all()
    if products and users:
        generate_cart.delay()
        return HttpResponse("Завдання розпочато")
    else:
        return HttpResponse("Спочатку треба згенерувати товари та користувачів!")


def order_view(request):
    categories = Category.objects.all()
    user = request.user
    if request.method == "POST":
        form = OrderForm(user, request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if user.social_auth.filter(provider="google-oauth2").exists():
                if "first_name" in form.cleaned_data:
                    user.first_name = form.cleaned_data["first_name"]
                if "last_name" in form.cleaned_data:
                    user.last_name = form.cleaned_data["last_name"]
                if "phone_number" in form.cleaned_data:
                    user.phone_number = form.cleaned_data["phone_number"]
                user.save()
            order.user = user
            cart = Cart.objects.get(user=user)
            order.cart = json.dumps(
                {
                    "items": [
                        {
                            "name": item.product.name,
                            "article": item.product.article,
                            "quantity": item.quantity,
                        }
                        for item in CartItem.objects.filter(cart=cart)
                    ]
                },
                ensure_ascii=False,
            )
            order.save()
            cart_item = CartItem.objects.filter(cart=cart)
            cart_item_list = []
            total_price = 0
            for item in cart_item:
                cart_item_list.append(f"{item.product.name}({item.product.article}) - {item.quantity} шт.")
                total_price += item.quantity * item.product.price.amount
            formatted_list = "\n".join(cart_item_list)
            send_mail(
                subject=f"Замовлення №{order.pk}!",
                message=f"Інформація про покупця:"
                f"\n\t1) Ім'я - {user.first_name}"
                f"\n\t2) Прізвище - {user.last_name}"
                f"\n\t3) Номер телефона - {user.phone_number}\n"
                f"Інформація про замовлення:"
                f"\n\t1) Спосіб доставки - {order.get_delivery_method_display()}"
                f"\n\t2) Спосіб оплати - {order.get_payment_method_display()}"
                f"\n\t3) Місто - {order.city}"
                f"\n\t4) Адреса відділення - {order.branch_address}\n"
                f"Товари:"
                f"\n{formatted_list}"
                f"\nДо сплати: {total_price}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[
                    "drobotda598@gmail.com",
                ],
                fail_silently=False,
            )
            Cart.objects.filter(user=user).delete()
            return render(request, "orders/order.html", {"form": form, "success_modal": True})
    else:
        form = OrderForm(user)

    return render(request, "orders/order.html", {"form": form, "categories": categories})
