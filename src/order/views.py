from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render  # NOQA: F401

from order.models import Cart, CartItem
from products.models import Product


def add_to_cart(request):
    return_dict = dict()
    data = request.POST
    product = get_object_or_404(Product, pk=data.get("product_id"))
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1

    cart_item.save()
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
