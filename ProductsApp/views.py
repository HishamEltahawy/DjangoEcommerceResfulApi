from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Products
from .serializers import SzProducts
from django.shortcuts import get_object_or_404
from .filters import ProductFilters
from rest_framework.permissions import IsAuthenticated 

# To get all products on database
@api_view(['GET'])
def get_all_products(response): # api/products/all-products/
    products = Products.objects.all()
    serializer = SzProducts(products, many=True)
    data_serialized = serializer.data
    return Response({'data':data_serialized})

# To get specific product.
@api_view(['GET'])
def get_one_product(request, pk): # api/products/one-product/<id-frontend>
    the_product = get_object_or_404(Products, id=pk)
    serializer = SzProducts(the_product, many=False)
    return Response({'data': serializer.data})

# To get products with filter 
@api_view(['GET'])
def get_filtered_products(request):
    products = Products.objects.all()
    filterset = ProductFilters(request.GET, products.order_by("id"))
    serializer = SzProducts(filterset.qs, many=True)
    return Response({'data': serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product(request):
    data = request.data
    data['user'] = request.user.id
    get_serializer = SzProducts(data=data)
    
    if get_serializer.is_valid():
        product = get_serializer.save(user=request.user)
        post_serializer = SzProducts(product, many=False)
        return Response({'product': post_serializer.data})
    else:
        return Response(get_serializer.errors)
