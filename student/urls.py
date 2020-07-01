from django.urls import path
from .views import *

urlpatterns = [
    path('list', student_list, name='student-list'),
    path('details/<int:id>', student_details, name='student-details')
]
