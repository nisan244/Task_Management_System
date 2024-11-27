from django.db import models
from Category.models import Category_Model
import datetime

# Create your models here.


class Task_Model(models.Model):
    task_Title = models.CharField(max_length= 100)
    task_Description = models.TextField()   
    category = models.ManyToManyField(Category_Model) 
    is_completed = models.BooleanField(default= False)
    assign_date = models.DateField(null= True, blank= True, default=datetime.date.today)
    
    
    def __str__(self):
        return self.task_Title
    