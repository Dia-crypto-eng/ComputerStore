from client.models import db,ClientCompanyLink,Payment
from invoice.models import BuyInvoice

# 4. PaymentInvoiceLinks
# LinkID
# IsPayment
# RelatedID

class PaymentInvoiceLink(db.Model):
    
    LINK_TYPE_CHOICES = [
        ('payment', 'Payment'),
        ('buyinvoice', 'BuyInvoice'),
    ]
    
    __name__="paymentInvoiceLink"
    link_id = db.AutoField(primary_key=True)
    #client = db.ForeignKey(ClientCompanyLink, on_delete=db.CASCADE)
    is_payment = db.CharField(max_length=10,choices=LINK_TYPE_CHOICES)
    related_payment = db.ForeignKey(Payment, null=True, blank=True, on_delete=db.CASCADE)
    related_buyinvoice = db.ForeignKey(BuyInvoice, null=True, blank=True, on_delete=db.CASCADE)

    def save(self, *args, **kwargs):
        # تحديد الحقول المرتبطة بناءً على قيمة is_payment
        if self.is_payment == 'payment':
            self.related_buyinvoice = None
        elif self.is_payment == 'buyinvoice':
            self.related_payment = None
        super().save(*args, **kwargs)

#     def __str__(self):
#         if self.is_payment == 'payment':
#             return f"Client: {self.client}, Payment ID: {self.related_payment.PaymentID}"
#         elif self.is_payment == 'buyinvoice':
#             return f"Client: {self.client}, Invoice ID: {self.related_buyinvoice.id}"
# #
#
#
#
#
#
#
#
#
#
# class PaymentInvoiceLink(db.Model):
    
#     LINK_TYPE_CHOICES = [
#         ('payment', 'Payment'),
#         ('buyinvoice', 'BuyInvoice'),
#     ]
    
#     __name__="paymentInvoiceLink"
#     link_id = db.AutoField(primary_key=True)
#     client = db.ForeignKey(ClientCompanyLink, on_delete=db.CASCADE)
#     is_payment = db.CharField(max_length=10,choices=LINK_TYPE_CHOICES)
#     related_payment = db.ForeignKey(Payment, null=True, blank=True, on_delete=db.CASCADE)
#     related_buyinvoice = db.ForeignKey(BuyInvoice, null=True, blank=True, on_delete=db.CASCADE)

#     def save(self, *args, **kwargs):
#         # تحديد الحقول المرتبطة بناءً على قيمة is_payment
#         if self.is_payment == 'payment':
#             self.related_invoice = None
#         elif self.is_payment == 'buyinvoice':
#             self.related_payment = None
#         super().save(*args, **kwargs)

#     def __str__(self):
#         if self.is_payment == 'payment':
#             return f"Client: {self.client}, Payment ID: {self.related_payment.PaymentID}"
#         elif self.is_payment == 'buyinvoice':
#             return f"Client: {self.client}, Invoice ID: {self.related_buyinvoice.id}"
