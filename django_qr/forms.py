from django import forms



class QRCodeForm(forms.Form):
    resurant_name = forms.CharField(label='Restaurant Name', max_length=100, widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Restaurant Name'})) # what is widget here
    url = forms.URLField(label='URL', max_length=200 , widget= forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter URL'}))
    