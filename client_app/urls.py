from django.urls import path 

from .views import create_employee, index
urlpatterns = [
    path('', index, name="client_index"),
    path('create_employee',create_employee, name="Create employee")
]