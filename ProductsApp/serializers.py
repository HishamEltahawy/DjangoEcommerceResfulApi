from rest_framework import serializers
from .models import Products

class SzProducts(serializers.ModelSerializer):
    class Meta():
        model = Products
        fields = ('name', 'brand', 'price', 'user')