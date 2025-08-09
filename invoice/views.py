from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .models import BuyInvoice,InvoiceItem,SellInvoice
from .serializers import InvoiceSerializer,InvoiceItemSerializer, SellInvoiceSerializer


@api_view(['GET'])
def get_all_invoice(request):
    invoice=BuyInvoice.objects.all()
    serializer=InvoiceSerializer(invoice,many=True)
    print(invoice)
    return Response( serializer.data)

@api_view(['GET'])
def get_id_invoice(request,ida):
    invoice=BuyInvoice.objects.get(id=ida)
    invoiceItem=InvoiceItem.objects.filter(invoice=invoice)

    # invoiceItem=InvoiceItem.objects.all()
    serializer=InvoiceItemSerializer(invoiceItem,many=True)
    

    # return Response( invoiceItem)
    return Response( serializer.data)

        
@api_view(['GET'])
def get_all_sell_invoice(request):
    invoice=SellInvoice.objects.all()
    serializer=SellInvoiceSerializer(invoice,many=True)
   
    return Response( serializer.data)        
        
        
# i=0
# for value in invoiceItem :
#     +(+i)    
#     dictvalue=value.__dict__
#     dictvalue.pop(next(iter(dictvalue)))
#     dict_you_want = {key: dictvalue[key] for key in {'price_buy','quantity'}}  