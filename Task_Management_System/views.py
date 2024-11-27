from django.shortcuts import render
from Tasks.models import Task_Model

def home(req):
    data = Task_Model.objects.all()
    return render(req, "home.html", {'data' : data})
    # return render(req, "home.html")