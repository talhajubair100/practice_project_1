from django.urls import path
from .views import *

urlpatterns = [
    path('detail/<int:id>', detail_post, name="detail-post"),
    path('category/<ctg_name>', category_by_list, name="category-list")

]
