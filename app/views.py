from django.shortcuts import render

# Create your views here.

from app.models import *


from django.http import HttpResponse


from app.forms import userForm


def register(request):

    if request.method == 'POST':

        name = request.POST['name']
        age  = request.POST['age']
        userdetails.objects.create(name=name,age = age)
        return HttpResponse("data inserted succesfully")
    return render(request,'register.html')  

def registerModelForm(request):
    uf = userForm()
    if request.method == 'POST':
        form_data = userForm(request.POST)
        if form_data.is_valid():
            print("data is valid")
            form_data.save()

            return HttpResponse("data is inserted successfully")
    return render(request,'registerModelForm.html',{'uf':uf})



def base(request,name):



    return render(request,'base.html',{'name':name})

