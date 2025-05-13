from rest_framework import serializers 
from client.models import ClientCompanyLink,Payment,Company
from invoice.models import Invoice,db
 
class ClientCompanyLinkSerializer(serializers.ModelSerializer):
    
    companyName = serializers.CharField(source='Company.CompanyName',read_only=True)
    crn = serializers.CharField(source='Company.CRN',max_length=50, required=False)
    nis = serializers.CharField(source='Company.NIS', max_length=50, required=False)
    nif = serializers.CharField(source='Company.NIF', max_length=50, required=False)
    email = serializers.EmailField(source='Client.Email')
    phoneNumber = serializers.CharField(source='Client.PhoneNumber', max_length=10, required=False)
    firstName = serializers.CharField(source='Client.FirstName', max_length=50, required=False)
    lastName = serializers.CharField(source='Client.LastName', max_length=50, required=False)
    
    class Meta:
        model = ClientCompanyLink
        # fields =   ('idInvoiceElement','invoice','price_buy','quantity')
        fields =   ('LinkID','companyName','crn','nis','nif','phoneNumber','email','firstName','lastName')




class ClientSummarySerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField(source='CompanyID')
    customer_name = serializers.CharField(source='CompanyName')
    total_purchases = serializers.SerializerMethodField()
    total_payments = serializers.SerializerMethodField()
    outstanding_balance = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ['customer_id', 'customer_name', 'total_purchases', 'total_payments', 'outstanding_balance']

    def get_total_purchases(self, obj):
        total_purchases = Invoice.objects.filter(
            paymentinvoicelink__client__in=ClientCompanyLink.objects.filter(Company=obj),
            paymentinvoicelink__is_payment='invoice'
        ).aggregate(total=db.Sum('amount'))['total'] or 0
        return total_purchases

    def get_total_payments(self, obj):
        total_payments = Payment.objects.filter(
            paymentinvoicelink__client__in=ClientCompanyLink.objects.filter(Company=obj),
            paymentinvoicelink__is_payment='payment'
        ).aggregate(total=db.Sum('AmountPaid'))['total'] or 0
        return total_payments

    def get_outstanding_balance(self, obj):
        total_purchases = self.get_total_purchases(obj)
        total_payments = self.get_total_payments(obj)
        return total_purchases - total_payments