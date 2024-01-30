from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .models import Invoice
from .serializers import InvoiceSerializer


@api_view(['GET'])
def get_all_invoice(request):
    invoice=Invoice.objects.all()
    serializer=InvoiceSerializer(invoice,many=True)
    print(invoice)
    return Response( serializer.data)