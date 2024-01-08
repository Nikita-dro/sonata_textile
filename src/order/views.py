from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render  # NOQA: F401
from django.views.generic import TemplateView

from order.models import Cart, CartItem
from products.models import Category, Product


def add_to_cart(request):
    return_dict = dict()
    data = request.POST
    product = get_object_or_404(Product, pk=data.get("product_id"))
    if data.get("update_quantity") and data.get("update_quantity") != "":
        quantity_action = data.get("update_action")
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(cart=cart, product=product)
        if quantity_action == "true":
            cart_item.quantity += 1
        else:
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
            else:
                cart_item.delete()
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
