from rest_framework import serializers
from ComputerStore.SumplifySerializer import DynamicFieldsModelSerializer
from .models import Invoice,InvoiceItem
from client.linkmodels import PaymentInvoiceLink
        
class InvoiceSerializer(DynamicFieldsModelSerializer):
    
    provider = serializers.SerializerMethodField()
    class Meta:
        model = Invoice
        fields = ('id','date','amount','provider')
        
    def get_provider(self, obj):
        # # #  # جمع الأسماء من الحقول المتاحة
        # # #  first_name = getattr(obj.provider, 'FirstName', '')
        # # #  last_name = getattr(obj.provider, 'LastName', '')
        # # #  return f"{first_name} {last_name}"
        
        # العثور على PaymentInvoiceLink المرتبطة بالفاتورة
        payment_invoice_link = PaymentInvoiceLink.objects.filter(related_invoice=obj).first()
        
        if payment_invoice_link:
            # العثور على ClientCompanyLink المرتبطة بـ PaymentInvoiceLink
            client_company_link = payment_invoice_link.client
            
            # الحصول على اسم الشركة من ClientCompanyLink
            company = client_company_link.Company
            
            # # الحصول على معلومات العميل من ClientCompanyLink
            # client = client_company_link.Client
            # company = client_company_link.Company
            # return {
            #     "ClientName": f"{client.FirstName} {client.LastName}",
            #     "CompanyName": company.CompanyName
            # }
            
            return company.CompanyName
        return None


class InvoiceItemSerializer(serializers.ModelSerializer):
    # ,fields=("name")
    # provider = serializers.RelatedField(source='invoice.provider', read_only=True) 
    # invoice=serializers.ModelSerializer(read_only=True)
    id = serializers.IntegerField(source='invoice.id',read_only=True)
    markProduct = serializers.CharField(source='product.mark',max_length=50, required=False)
    nameProduct = serializers.CharField(source='product.name',allow_blank=True, max_length=50, required=False)
    amount = serializers.SerializerMethodField()

    
    class Meta:
        model = InvoiceItem
        # fields =   ('idInvoiceElement','invoice','price_buy','quantity')
        fields =   ('id','idInvoiceElement','markProduct','nameProduct','price_buy','quantity','amount')
    
    def get_amount(self,obj):
        
        return obj.price_buy*obj.quantity
        
    # Invoice_Item_FIELDS = ['idInvoiceElement', 'id', 'name','brand','price_buy','quantity']
    # idInvoiceElement = serializers.IntegerField(label='IdInvoiceElement', read_only=True)
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(allow_blank=True, max_length=50, required=False)
    # brand = serializers.CharField(max_length=50, required=False)
    # price_buy = serializers.FloatField(required=False)
    # quantity = serializers.IntegerField(max_value=9223372036854775807, min_value=-9223372036854775808, required=False)
 

     