from django.shortcuts import redirect, render
from employee_register.forms import EmployeeForm
from employee_register.models import Employee
from .forms import EmployeeForm
# Create your views here.
def employee_list(request):
    return render(request,"employee_register/employee_list.html")

def employee_form(request):
    if request.method=="GET":
       form=EmployeeForm()
       return render(request,"employee_register/employee_form.html",{'form':form})
    else:
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_delete(request):
    return