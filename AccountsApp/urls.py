from django.urls import path, include
from AccountsApp import views

urlpatterns = [

    # Apps paths
    # api/accounts/
    path('register/', views.register), # register/
    path('current_user/', views.current_user), # current_user/
    path('update_user/', views.update_user), # update_user/
    path('forget_password/', views.forget_password), # forget_password/
    path('reset_password/<str:token>', views.reset_password), # reset_password/
]