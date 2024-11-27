from django import forms
from . import models


class category_Form(forms.ModelForm):
    class Meta:
        model = models.Category_Model
        fields = '__all__'
        
        
        labels = {
            'name' : "Category",
        }
        
        
