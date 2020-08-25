from .models import Product, Review
from rest_framework import serializers

'''
Este nuevo serializador Reviews estará asociado a los Productos

Note: When we serialise the user contained in created_by field, return the 
username instead of the id (to make it more human readable)

'''
class ReviewSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Review
        fields = ('id', 'title', 'review', 'rating', 'created_by')


'''
El field 'reviews' sería la vinculación entre los serializadores teniendo
presente la definición correcta del campo related_name en el modelo Review
'''
class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        # se agrega el id del producto para usarse en ProductDetail
        fields = ('id', 'name', 'description', 'price', 'reviews')