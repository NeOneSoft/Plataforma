# Tastypie
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

# Models
from .models import Product


class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'bulk_insert'
        authorization = Authorization()


class GetProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'products'
        fields = ['name', 'value', 'discount_value', 'stock']
