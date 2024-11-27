from django import forms
from . import models


class task_Form(forms.ModelForm):
    class Meta:
        model = models.Task_Model
        fields = '__all__'
        
        
        
        labels = {
            'task_Title' : 'Title',
            'task_Description' : 'Description',
            'is_completed' : 'Complete',
            
        }
        
        widgets = {
            'assign_date' : forms.DateInput(attrs={'type': 'date'}),
            
        }
        
        
