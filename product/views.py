from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer


@api_view(['GET'])
def get_all_category(request):
    category=Category.objects.all()
    serializer=CategorySerializer(category,many=True)

    return Response( serializer.data)