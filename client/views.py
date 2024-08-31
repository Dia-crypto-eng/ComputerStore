from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from client.models import ClientCompanyLink,Company
from client.linkmodels import PaymentInvoiceLink
from client.serializers import ClientCompanyLinkSerializer,ClientSummarySerializer


@api_view(['GET'])
def get_all_company(request):
    company=ClientCompanyLink.objects.all()
    serializer=ClientCompanyLinkSerializer(company,many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def get_all_Financial_Status(request):
    company=Company.objects.all()
    serializer=ClientSummarySerializer(company,many=True)
    
    return Response(serializer.data)