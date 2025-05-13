from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer,ProductPostSerializer

@api_view(['POST'])
def post_product(request):
    serializer=ProductPostSerializer(data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def get_all_category(request):
    category=Category.objects.all()
    serializer=CategorySerializer(category,many=True)

    return Response( serializer.data)

@api_view(['GET'])
def get_product_by_category(request,category):
    category=Category.objects.get(name=category)
    # product=Product.objects.filter(category=id)
    product=category.products.all()
    serializer=ProductSerializer(product,many=True)
    return Response( serializer.data)
    # return Response( "test")