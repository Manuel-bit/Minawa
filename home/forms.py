from django.forms import ModelForm
from .models import Quotation

class QuotationForm(ModelForm):
    class Meta:
        model = Quotation
        fields = ['customer_name', 'customer_email', 'message']