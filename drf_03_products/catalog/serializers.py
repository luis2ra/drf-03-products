from django.contrib.auth.models import User
from .models import Product, Review
from rest_framework import serializers

'''
Este nuevo serializador Reviews estará asociado a los Productos

Note: When we serialise the user contained in created_by field, return the 
username instead of the id (to make it more human readable)

'''
class ReviewSerializer(serializers.ModelSerializer):
    # created_by = serializers.ReadOnlyField(source='created_by.id')

    class Meta:
        model = Review
        fields = ('id', 'title', 'review', 'rating', 'created_by')
        #fields = ('id', 'title', 'review', 'rating')


'''
El field 'reviews' sería la vinculación entre los serializadores teniendo
presente la definición correcta del campo related_name en el modelo Review
'''
class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        # se agrega el id del producto para usarse en ProductDetail
        fields = ('id', 'name', 'description', 'price', 'reviews')

    def create(self, validated_data):
        print(validated_data)
        # validated_data['id']=9
        # print(validated_data)        
        reviews_data = validated_data.pop('reviews')
        print(reviews_data)
        product = Product.objects.create(**validated_data)
        print('------------------------------------------------------------')
        print(product.id)
        print('------------------------------------------------------------')
        i = int(100)
        for review_data in reviews_data:
            # print(review_data)
            # review_data['id']= i
            # i = i + 1
            print(review_data)
            Review.objects.create(product=product, **review_data)
        return product

    