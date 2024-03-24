from rest_framework import serializers
from ComputerStore.SumplifySerializer import DynamicFieldsModelSerializer
from product.models import Product
from .models import Invoice,InvoiceItem
from product.serializers import ProductSerializer


        
class InvoiceSerializer(DynamicFieldsModelSerializer):
    
    class Meta:
        model = Invoice
        fields = "__all__"


class InvoiceItemSerializer(serializers.ModelSerializer):
    # ,fields=("name")
    # provider = serializers.RelatedField(source='invoice.provider', read_only=True) 
    # invoice=serializers.ModelSerializer(read_only=True)
    id = serializers.IntegerField(source='invoice.id',read_only=True)
    markProduct = serializers.CharField(source='product.brand',max_length=50, required=False)
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
 
#  Id = 111,
#  IdFactureElement = 122,
#  CategoryProduct = "SSS",
#  MarkProduct = "RRRRR",
#  NameProduct = "TTTTtttttttttttttttttt",
#  Price_buy = 333,
#  Quantity = 4,
#  Amount = 5555 },
     