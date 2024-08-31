from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_all_company),
    path('Finance',views.get_all_Financial_Status),
    
    
]