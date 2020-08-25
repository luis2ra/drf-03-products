from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        # se agrega el id del producto para usarse en ProductDetail
        fields = ('id', 'name', 'description', 'price')