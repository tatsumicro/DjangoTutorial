from django import forms
from .models import Item, Shop, Stock


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'cost', 'description']
        

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name']
        
        
class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['shop', 'item', 'num']