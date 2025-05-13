from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_product,name=''),
    path('category',views.get_all_category,name=''),
    path('<str:category>',views.get_product_by_category,name='')
]