from products.models import Brand, Category, ProducingCountry, Product


def sample_product(article: int, name: str, size: str, price: float, **params) -> Product:
    default = {
        "category": Category.objects.create(name="TestCategory"),
        "brand": Brand.objects.create(name="TestBrand"),
        "material": "TestMaterial",
        "producing_country": ProducingCountry.objects.create(name="TestProducingCountry"),
        "description": "TestDescription",
    }
    default.update(params)
    return Product.objects.create(article=article, name=name, size=size, price=price, **default)
