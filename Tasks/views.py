from django.shortcuts import render, redirect
from . import forms, models


# Create your views here.

def add_task(req):
    if req.method == "POST":
        task_form = forms.task_Form(req.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect("add_task")
        
    else:
        task_form = forms.task_Form()
    
    return render(req, 'add_task.html', {'form' : task_form})


def edit_task(req, id):
    task = models.Task_Model.objects.get(pk = id)
    task_form = forms.task_Form(instance = task)
    
    if req.method == "POST":
        task_form = forms.task_Form(req.POST, instance = task)
        if task_form.is_valid():
            task_form.save()
            return redirect("home")
    
    return render(req, 'add_task.html', {'form' : task_form})



def delete_task(req, id):
    task = models.Task_Model.objects.get(pk = id).delete()
    return redirect("home")

