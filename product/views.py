from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


@api_view(['GET'])
def get_all_category(request):
    category=Category.objects.all()
    serializer=CategorySerializer(category,many=True)

    return Response( serializer.data)

@api_view(['GET'])
def get_product_by_category(request,category):
    id=Category.objects.get(name=category)
    product=Product.objects.filter(category=id)
    serializer=ProductSerializer(product,many=True)
    return Response( serializer.data)
    # return Response( "test")