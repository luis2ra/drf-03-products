from django.http import Http404

from rest_framework.generics import (ListCreateAPIView, 
                                    RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )


class ReviewList(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    '''
    As you can notice, I had to customise the perform_create method because 
    the default one doesn't know anything about the fact we want to set the 
    created_by and product_id fields.
    '''
    def perform_create(self, serializer):
        print(self.request.user.pk)
        serializer.save(
            created_by=self.request.user.id,
            product_id=self.kwargs['pk'])


class ReviewDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    lookup_url_kwarg = 'review_id'

    def get_queryset(self):
        review = self.kwargs['review_id']
        return Review.objects.filter(id=review)