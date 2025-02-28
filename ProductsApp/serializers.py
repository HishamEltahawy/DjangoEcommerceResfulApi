from rest_framework import serializers
from .models import Products, Reviews

class SzReview(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class SzProducts(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(method_name='get_reviews', read_only=True)

    class Meta:
        model = Products
        fields = '__all__'

    def get_reviews(self, obj):
        reviews = obj.reviews.all()
        serializer = SzReview(reviews, many=True)
        return serializer.data
