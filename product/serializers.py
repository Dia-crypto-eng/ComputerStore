from rest_framework import serializers
from .models import Product
from ComputerStore.SumplifySerializer import DynamicFieldsModelSerializer

class ProductSerializer(DynamicFieldsModelSerializer):
    
    class Meta:
        model = Product
        fields = "__all__"
                
        


        

     