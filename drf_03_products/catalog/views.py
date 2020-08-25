from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsAdminOrReadOnly


'''
Con ListAPIView se debe implementar la función "post".  No hacerlo la vista de 
tipo List queda sólo de lectura con implementación nativa de GET.

Con ListCreateAPIView internamente implementa GET y POST
'''
class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )