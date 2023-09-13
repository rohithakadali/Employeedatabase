from django.shortcuts import render
from salary.models import Employee

def home(request):
    employees = Employee.objects.all()
    print(employees)
    context = {
        'employees':employees,
    }
    return render(request,'home.html',context)
