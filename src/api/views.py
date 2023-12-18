from django.contrib.auth import get_user_model
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from api.serializers import (BrandSerializer, CartCreateUpdateSerializer,
                             CartItemCreateUpdateSerializer,
                             CartItemSerializer, CartSerializer,
                             CategorySerializer, CitySerializer,
                             CustomerSerializer, ProducingCountrySerializer,
                             ProductCreateUpdateSerializer, ProductSerializer)
from order.models import Cart, CartItem, City
from products.models import Brand, Category, ProducingCountry, Product


class CustomerCreate(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomerSerializer


class CustomerUpdate(UpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomerSerializer


class CustomerDelete(DestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomerSerializer


class CustomerListAll(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomerSerializer


class CustomerListOne(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomerSerializer


class ProductListAll(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListOne(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreate(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateUpdateSerializer


class ProductUpdate(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateUpdateSerializer


class ProductDelete(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProducingCountryViewSet(ModelViewSet):
    queryset = ProducingCountry.objects.all()
    serializer_class = ProducingCountrySerializer


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


# class CartViewSet(ModelViewSet):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer
#
#
# class CartItemViewSet(ModelViewSet):
#     queryset = CartItem.objects.all()
#     serializer_class = CartItemSerializer


class CartListAll(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartListOne(RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartCreate(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartCreateUpdateSerializer


class CartUpdate(UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartCreateUpdateSerializer


class CartDelete(DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemListAll(ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartItemListOne(RetrieveAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartItemCreate(CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemCreateUpdateSerializer


class CartItemUpdate(UpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemCreateUpdateSerializer


class CartItemDelete(DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
