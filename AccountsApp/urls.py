from django.urls import path, include
from AccountsApp import views

urlpatterns = [

    # Apps paths
    path('register/', views.register), # api/accounts/register/
    path('current_user/', views.current_user), # api/accounts/current_user/
]