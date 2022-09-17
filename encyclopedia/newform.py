
from django import forms


class NewForm(forms.Form):
    title = forms.CharField(label="New Entry Title", max_length=128,min_length=1,
                            required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label="Enter Markdown Content", min_length=5, widget=forms.Textarea(attrs={'class': 'form-control'}),
                              required=True)