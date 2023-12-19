from django.contrib.auth import get_user_model
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from api.serializers import (BrandSerializer, CategorySerializer,
                             CitySerializer, CustomerSerializer,
                             ProducingCountrySerializer,
                             ProductCreateUpdateSerializer, ProductSerializer)
from order.models import City
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
