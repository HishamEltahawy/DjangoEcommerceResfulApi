# DjangoEcommerceResfulApi
Ecommerce web application using Django-Restful-Framework  
Django Ecommerce RESTful API Documentation
Overview
This project is a RESTful API for an ecommerce platform built using Django and Django REST framework. It includes functionalities for user registration, authentication, product management, order processing, and more.

Project Structure
Installation
Clone the repository:

Create a virtual environment and activate it:

Install the dependencies:

Apply the migrations:

Create a superuser:

Run the development server:

API Endpoints
AccountsApp
User Registration
URL: /api/accounts/register/
Method: POST
Description: Registers a new user.
Request Body:
Response:
Forget Password
URL: /api/accounts/forget_password/
Method: POST
Description: Sends a password reset link to the user's email.
Request Body:
Response:
Reset Password
URL: /api/accounts/reset_password/<token>/
Method: POST
Description: Resets the user's password using the provided token.
Request Body:
Response:
OrdersApp
Get All Orders
URL: /api/orders/
Method: GET
Description: Retrieves all orders.
Response:
Get One Order
URL: /api/orders/<pk>/
Method: GET
Description: Retrieves a single order by its ID.
Response:
Process Order
URL: /api/orders/<pk>/process/
Method: PUT
Description: Updates the status of an order.
Request Body:
Response:
Delete Order
URL: /api/orders/<pk>/
Method: DELETE
Description: Deletes an order by its ID.
Response:
Create New Order
URL: /api/orders/new/
Method: POST
Description: Creates a new order.
Request Body:
Response:
ProductsApp
Get All Products
URL: /api/products/
Method: GET
Description: Retrieves all products.
Response:
Get One Product
URL: /api/products/<pk>/
Method: GET
Description: Retrieves a single product by its ID.
Response:
Create New Product
URL: /api/products/new/
Method: POST
Description: Creates a new product.
Request Body:
Response:
Update Product
URL: /api/products/<pk>/
Method: PUT
Description: Updates an existing product.
Request Body:
Response:
Delete Product
URL: /api/products/<pk>/
Method: DELETE
Description: Deletes a product by its ID.
Response:
Models
AccountsApp
Profile
Fields:
user: ForeignKey to User
new_token: CharField
ex_date: DateTimeField
OrdersApp
Order
Fields:
user: ForeignKey to User
city: CharField
zip_code: CharField
street: CharField
phone_no: CharField
country: CharField
total_amount: FloatField
status: CharField
created_at: DateTimeField
updated_at: DateTimeField
OrderItem
Fields:
product: ForeignKey to Product
order: ForeignKey to Order
name: CharField
quantity: IntegerField
price: FloatField
ProductsApp
Product
Fields:
name: CharField
description: TextField
price: FloatField
stock: IntegerField
created_at: DateTimeField
updated_at: DateTimeField
Serializers
AccountsApp
SzSignup
Fields:
username
first_name
last_name
email
password
SzUsers
Fields:
username
first_name
last_name
email
OrdersApp
OrderSerializer
Fields:
id
user
city
zip_code
street
phone_no
country
total_amount
status
created_at
updated_at
ProductsApp
ProductSerializer
Fields:
id
name
description
price
stock
created_at
updated_at
Permissions
IsAuthenticated: Ensures that the user is authenticated.
IsAdminUser: Ensures that the user is an admin.
Conclusion
This documentation provides an overview of the Django Ecommerce RESTful API project, including installation instructions, API endpoints, models, serializers, and permissions. This should help you understand and work with the project effectively. If you have any questions or need further assistance, feel free to reach out.