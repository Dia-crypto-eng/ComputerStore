from rest_framework import serializers
from .models import Product,Category
from ComputerStore.SumplifySerializer import DynamicFieldsModelSerializer

class ProductSerializer(DynamicFieldsModelSerializer):
    
    class Meta:
        model = Product
        fields = "__all__"
        
class CategorySerializer(DynamicFieldsModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"

                
        


        

     