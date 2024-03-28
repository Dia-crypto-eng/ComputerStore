from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .models import Invoice,InvoiceItem
from .serializers import InvoiceSerializer,InvoiceItemSerializer


@api_view(['GET'])
def get_all_invoice(request):
    invoice=Invoice.objects.all()
    serializer=InvoiceSerializer(invoice,many=True)
    print(invoice)
    return Response( serializer.data)

@api_view(['GET'])
def get_id_invoice(request,ida):
    invoice=Invoice.objects.get(id=ida)
    invoiceItem=InvoiceItem.objects.filter(invoice=invoice)

    # invoiceItem=InvoiceItem.objects.all()
    serializer=InvoiceItemSerializer(invoiceItem,many=True)
    

    # return Response( invoiceItem)
    return Response( serializer.data)

        
        
        
        
# i=0
# for value in invoiceItem :
#     +(+i)    
#     dictvalue=value.__dict__
#     dictvalue.pop(next(iter(dictvalue)))
#     dict_you_want = {key: dictvalue[key] for key in {'price_buy','quantity'}}  