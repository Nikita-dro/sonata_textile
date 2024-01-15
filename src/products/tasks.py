from celery import shared_task

from products.models import (Brand, Category, Material, ProducingCountry,
                             Product)


@shared_task
def generate_categories(count: int):
    Category.generate_instances(count)


@shared_task
def generate_producing_country(count: int):
    ProducingCountry.generate_instances(count)


@shared_task
def generate_brand(count: int):
    Brand.generate_instances(count)


@shared_task
def generate_material(count: int):
    Material.generate_instances(count)


@shared_task
def generate_product(count: int):
    Product.generate_instances(count)
