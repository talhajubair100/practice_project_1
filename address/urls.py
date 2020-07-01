from django.urls import path
from .views import *

urlpatterns = [
    path('district', district_list, name='district-list'),
    path('district/details/<int:id>', district_details, name='district-details'),

]
