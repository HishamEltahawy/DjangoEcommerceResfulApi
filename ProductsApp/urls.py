from django.urls import path, include
from ProductsApp import views

urlpatterns = [

    # Apps paths
    # api/products/
    path('all-products/', views.get_all_products), # all-products/
    path('one-product/<str:pk>/', views.get_one_product), # one-product/<id>  
    path('get_filtered_products/', views.get_filtered_products),
    # get_filtered_products/?catagory=<brandName-frontend>
    # get_filtered_products/?user=<brandName-frontend>
    # get_filtered_products/?brand=<brandName-frontend>
    # get_filtered_products/?keyword=<price-frontend>
    # get_filtered_products/?minPrice=<price-frontend>
    # get_filtered_products/?maxPrice=<price-frontend>  
    path('add_product/', views.add_product),  # add_product/
    
]
