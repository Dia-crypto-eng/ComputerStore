from rest_framework import serializers
from .models import Inventory
#from ComputerStore.SumplifySerializer import DynamicFieldsModelSerializer,'location'




class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"
        
      



