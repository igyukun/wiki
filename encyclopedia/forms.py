# forms.py file contains the Django Forms classes

from django import forms


class NewEntryForm(forms.Form):
    """
    The NewEntryForm class inherites a Django forms.Form 
    It is instantiated when creating a new form for new entry creation.
    It contains two fields: 
    - entry title using TextInput widget 
    - entry content using Textarea widget
    The class fields use Bootstrap5 classes for an HTML decoration
    """
    title = forms.CharField(label="New Entry Title", max_length=128,min_length=1,
                            required=True, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    content = forms.CharField(label="Enter Markdown Content", min_length=5, required=True, 
                              widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    
class EditForm(forms.Form):
    """
    The EditForm class inherites a Django forms.Form
    It is instantiated for existing entry editing.
    It contains one field: 
    - entry content using Textarea widget
    The class fields use Bootstrap5 classes for an HTML decoration
    """
    content = forms.CharField(label="Enter Markdown Content", min_length=5, widget=forms.Textarea(attrs={'class': 'form-control'}),
                              required=True)
