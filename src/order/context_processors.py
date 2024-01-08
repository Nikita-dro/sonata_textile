from order.models import Cart, CartItem


def getting_basket_info(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        products_number = CartItem.objects.filter(cart=cart)
        total = 0
        total_price = 0
        for cart_item_obj in products_number:
            total += cart_item_obj.quantity
            total_price += cart_item_obj.quantity * cart_item_obj.product.price.amount
    return locals()
