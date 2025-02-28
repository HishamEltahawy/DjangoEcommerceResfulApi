from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated ,IsAdminUser
from rest_framework import status
from ProductsApp.models import Products
from .serializers import OrderSerializer
from .models import Order,OrderItem
# Create your views here.

"""
This function retrieves all orders from the database and serializes them before returning a response
with the order data.

:param request: The `request` parameter in the `get_all_orders` function is an object that contains
information about the current HTTP request, such as the request method, headers, user authentication
details, and any data sent in the request body. It allows you to access and interact with the
incoming request data in your
:return: A response containing a JSON object with the key 'orders' and the serialized data of all
orders retrieved from the database.
"""
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders,many=True)
    return Response({'orders':serializer.data})

"""
This function retrieves a single order object by its primary key and returns its serialized data.

:param request: The `request` parameter in the `get_one_order` function is an object that contains
information about the current HTTP request, such as the request method, headers, user authentication
details, and query parameters. It is passed automatically by Django REST framework when a view
function is called in response to a request
:param pk: The `pk` parameter in the `get_one_order` function stands for "primary key" and is used
to identify a specific order in the database. In this case, it is used to retrieve a single order
object based on its primary key value
:return: A response containing the data of a single order serialized using the OrderSerializer is
being returned. The response includes the order data in JSON format.
"""
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_one_order(request,pk):
    order =get_object_or_404(Order, id=pk)

    serializer = OrderSerializer(order,many=False)
    return Response({'order':serializer.data})


"""
This function updates the status of an order with the provided ID.

:param request: The `request` parameter in the `process_order` function is an object that contains
information about the current HTTP request. It includes details such as the request method (PUT in
this case), request data, headers, user authentication details, and more. In this function, we are
using the request to
:param pk: The `pk` parameter in the `process_order` function represents the primary key of the
order that is being processed. It is used to retrieve the specific order from the database based on
its primary key value
:return: The code snippet is returning a response containing the serialized data of the updated
order after processing the order status. The response includes the order details in JSON format.
"""
@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsAdminUser])
def process_order(request,pk):
    order =get_object_or_404(Order, id=pk)
    order.status = request.data['status']
    order.save()
     
    serializer = OrderSerializer(order,many=False)
    return Response({'order':serializer.data})

"""
This function deletes an order with a specific ID after checking if the user is authenticated.

:param request: The `request` parameter in the `delete_order` function represents the HTTP request
that is sent to the server when the API endpoint is accessed. It contains information such as the
request method, headers, data, and user authentication details. In this case, the function is
expecting a DELETE request to delete
:param pk: The `pk` parameter in the `delete_order` function stands for the primary key of the order
that you want to delete. It is used to uniquely identify the order that needs to be deleted from the
database
:return: a Response object with a dictionary containing the details message "order is deleted".
"""
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_order(request,pk):
    order =get_object_or_404(Order, id=pk) 
    order.delete()
      
    return Response({'details': "order is deleted"})


"""
This function creates a new order for a user by processing the order items and updating product
stock levels.

:param request: The code snippet you provided is a Django view function for creating a new order.
Let me explain the parameters used in the view function:
:return: The code snippet is a Django REST framework view function for creating a new order. It
takes a POST request with order data, validates the data, calculates the total amount, creates an
Order object, creates OrderItem objects for each item in the order, updates the product stock, and
returns the serialized Order object as a response.
"""
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_order(request):
    user = request.user 
    data = request.data
    order_items = data['order_Items']

    if order_items and len(order_items) == 0:
       return Response({'error': 'No order recieved'},status=status.HTTP_400_BAD_REQUEST)
    else:
        total_amount = sum( item['price']* item['quantity'] for item in order_items)
        order = Order.objects.create(
            user = user,
            city = data['city'],
            zip_code = data['zip_code'],
            street = data['street'],
            phone_no = data['phone_no'],
            country = data['country'],
            total_amount = total_amount,
        )
        for i in order_items:
            product = Products.objects.get(id=i['product'])
            item = OrderItem.objects.create(
                product= product,
                order = order,
                name = product.name,
                quantity = i['quantity'],
                price = i['price']
            )
            product.stock -= item.quantity
            product.save()
        serializer = OrderSerializer(order,many=False)
        return Response(serializer.data)