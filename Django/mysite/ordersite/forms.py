from django import forms

from ordersite import models

class OrderReportForm(forms.Form):
    ordernumber = forms.CharField(label='ordernumber')