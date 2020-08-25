from django.urls import path
from . import views
from catalog.views import ProductList, ProductDetail

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('products/<int:pk>/reviews/', views.ReviewList.as_view()),
]