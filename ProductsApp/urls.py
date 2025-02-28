from django.urls import path, include
from ProductsApp import views

urlpatterns = [

    # Apps paths
    # api/products/
    path('all_products/', views.get_all_products), # all_products/
    path('one_product/<str:pk>/', views.get_one_product), # one_product/<id>  
    path('get_filtered_products/', views.get_filtered_products),
    # get_filtered_products/?catagory=<brandName-frontend>
    # get_filtered_products/?user=<brandName-frontend>
    # get_filtered_products/?brand=<brandName-frontend>
    # get_filtered_products/?keyword=<price-frontend>
    # get_filtered_products/?minPrice=<price-frontend>
    # get_filtered_products/?maxPrice=<price-frontend>  
    path('add_product/', views.add_product),  # add_product/
    path('update_product/<str:pk>/', views.update_product), # update_product/<id>  
    path('delete_product/<str:pk>/', views.delete_product), # update_product/<id>  
    path('add_review/<str:pk>/', views.add_review), # update_product/<id>  
    path('delete_review/<str:pk>/', views.add_review), # delete_review/<id>  
   
    
]
