from django.urls import path
from . import views

urlpatterns = [
    path('category',views.get_all_category,name='')
]