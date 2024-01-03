from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render  # NOQA: F401

from order.models import Cart, CartItem
from products.models import Product


# Create your views here.
def add_to_cart(request):
    # product = get_object_or_404(Product, pk=product_id)
    #
    # cart, created = Cart.objects.get_or_create(user=request.user)
    #
    # cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    #
    # cart_item.quantity += 1
    # cart_item.save()
    # print("dfkj")
    # data = {
    #     "product_name": product.name,
    #     "quantity": cart_item.quantity,
    # }
    # return JsonResponse(data)
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product = get_object_or_404(Product, pk=product_id)

        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
        # Добавление товара в корзину (замените на свой код)
        # Предположим, что у вас есть модель CartItem с полями user, product и quantity
        # cart_item = CartItem.objects.create(user=request.user, product_id=product_id, quantity=1)

        return JsonResponse({"message": "Товар успешно добавлен в корзину!"})
    return JsonResponse({"message": "Метод не разрешен"}, status=405)
