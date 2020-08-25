from django.urls import path
from . import views
from catalog.views import ProductList

urlpatterns = [
    path('products/', ProductList.as_view()),
]