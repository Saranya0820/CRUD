from django.shortcuts import render,redirect
from .models import Employee

def index(request):
    data=Employee.objects.all()
    context={"data":data}
    return render(request,"index.html",context)

def insertData(request):
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        address = request.POST.get('address')
        gender=request.POST.get('gender')
        print(name,email,age,address,gender)
        employee=Employee(name=name,email=email,age=age,address=address,gender=gender)
        employee.save()
        return redirect("/")

    return render(request,"index.html")


def updateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        address = request.POST['address']
        gender=request.POST['gender']

        edit=Employee.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.address=address
        edit.gender=gender
        edit.save()
        return redirect("/")

    d=Employee.objects.get(id=id)
    context={"d":d}

    return render(request,"update.html",context)

def deleteData(request,id):

    data=Employee.objects.get(id=id)
    data.delete()
    return redirect("/")
