from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_all_invoice,name=''),
    path('<int:ida>',views.get_id_invoice),
    path('sell',views.get_all_sell_invoice),
    
]
