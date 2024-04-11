from django.urls import path
from . import views

urlpatterns = [
    path('category',views.get_all_category,name=''),
    path('<str:category>',views.get_product_by_category,name='')
]