from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .models import Inventory
from .serializers import InventorySerializer


# Create your views here.
@api_view(['GET'])
def get_all_inventory(request):
    inventory=Inventory.objects.all()
    serializer=InventorySerializer(inventory,many=True)
    print(inventory)
    return Response( serializer.data)