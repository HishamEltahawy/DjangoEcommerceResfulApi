from django.urls import path
from . import views

# This code snippet is defining URL patterns for a Django application. Each `path` function call
# specifies a URL pattern along with the corresponding view function that should be called when that
# URL is accessed.
urlpatterns = [
    path('new_order/', views.new_order,name='new_order'), 
    path('get_all_orders/', views.get_all_orders,name='get_all_orders'), 
    path('get_one_order/<str:pk>/', views.get_one_order,name='get_one_order'), 

    path('process_order/<str:pk>/process/', views.process_order,name='process_order'), 
    path('delete_order/<str:pk>/delete/', views.delete_order,name='delete_order'), 

]