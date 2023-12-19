from django.contrib.auth import get_user_model
from rest_framework.fields import CharField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from order.models import City
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
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    producing_country = ProducingCountrySerializer(read_only=True)

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
