from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

'''
Probamos el uso de ListCreateAPIView en vez de ListAPIView
Esta clase trae por defecto la implementación del método POST
'''
class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer