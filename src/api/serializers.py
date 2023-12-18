from django.contrib.auth import get_user_model
from rest_framework.fields import CharField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from order.models import Cart, CartItem, City
from products.models import Brand, Category, ProducingCountry, Product


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "first_name", "last_name", "email", "phone_number", "is_staff")


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ("id", "name")


class ProducingCountrySerializer(ModelSerializer):
    class Meta:
        model = ProducingCountry
        fields = ("id", "name")


class ProductSerializer(ModelSerializer):
    price = CharField()
    category = CategorySerializer()
    brand = BrandSerializer()
    producing_country = ProducingCountrySerializer()

    class Meta:
        model = Product
        fields = (
            "id",
            "article",
            "name",
            "avatar",
            "category",
            "brand",
            "price",
            "size",
            "material",
            "producing_country",
            "availability",
            "hit_sale",
            "description",
        )


class ProductCreateUpdateSerializer(ProductSerializer):
    category = PrimaryKeyRelatedField(queryset=Category.objects.all())
    brand = PrimaryKeyRelatedField(queryset=Brand.objects.all())
    producing_country = PrimaryKeyRelatedField(queryset=ProducingCountry.objects.all())


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name")


# class CartItemSerializer(ModelSerializer):
#     product = PrimaryKeyRelatedField(queryset=Product.objects.all())
#     cart = PrimaryKeyRelatedField(queryset=Cart.objects.all())
#
#     class Meta:
#         model = CartItem
#         fields = "__all__"
#
#
# class CartItemCreateUpdateSerializer(CartItemSerializer):
#     cart = CartSerializer
#
#     class Meta:
#         model = CartItem
#         fields = "__all__"


class CartItemSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ("id", "cart", "product", "quantity")


class CartItemCreateUpdateSerializer(CartItemSerializer):
    product = PrimaryKeyRelatedField(queryset=Product.objects.all())
    cart = PrimaryKeyRelatedField(queryset=Cart.objects.all())


class CartSerializer(ModelSerializer):
    user = CustomerSerializer()
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ("id", "user", "items")


class CartCreateUpdateSerializer(CartSerializer):
    user = PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    items = PrimaryKeyRelatedField(queryset=CartItem.objects.all())
    # items = PrimaryKeyRelatedField(queryset=Product.objects.all())


# class CartItemSerializer(ModelSerializer):
#     product = ProductSerializer(many=True, read_only=True)
#     cart = CartSerializer(many=True, read_only=True)
#
#     # cart = PrimaryKeyRelatedField(queryset=Cart.objects.all())
#
#     class Meta:
#         model = CartItem
#         fields = "__all__"
