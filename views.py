from collections import UserList
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from .forms import AirfreightForm, EmployeeForm, LCLForm
from .models import LCL, Airfreight, Employee
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from employee_project.decorators import *
from users import *


###########################################################################################################
@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def FCL_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/FCL_list.html", context)


@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def FCL_form(request, id=0):

    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/FCL_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form = form.save(commit=False)
            user_id = request.user.pk
            form.username = User.objects.get(pk=user_id)
            form.save()
        return redirect('/main/FCL_list.html')


@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def FCL_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/main/FCL_list.html')

###########################################################################################################


@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def AIR_list(request):
    context = {'airfreight_list': Airfreight.objects.all()}
    return render(request, "employee_register/AIR_list.html", context)


@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def AIR_form(request, id=0):

    if request.method == "GET":
        if id == 0:
            form = AirfreightForm()
        else:
            airfreight = Airfreight.objects.get(pk=id)
            form = AirfreightForm(instance=airfreight)
        return render(request, "employee_register/AIR_form.html", {'form': form})
    else:
        if id == 0:
            form = AirfreightForm(request.POST)
        else:
            airfreight = Airfreight.objects.get(pk=id)
            form = AirfreightForm(request.POST, instance=airfreight)
        if form.is_valid():
            form = form.save(commit=False)
            user_id = request.user.pk
            form.username = User.objects.get(pk=user_id)
            form.save()
        return redirect('/main/AIR_list.html')


@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def AIR_delete(request, id):
    airfreight = Airfreight.objects.get(pk=id)
    airfreight.delete()
    return redirect('/main/AIR_list.html')

###########################################################################################################


@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def LCL_list(request):
    context = {'lcl_list': LCL.objects.all()}
    return render(request, "employee_register/LCL_list.html", context)


@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def LCL_form(request, id=0):
    
    if request.method == "GET":
        if id == 0:
            form = LCLForm()
        else:
            lcl = LCL.objects.get(pk=id)
            form = LCLForm(instance=lcl)
        return render(request, "employee_register/LCL_form.html", {'form': form})
    else:
        if id == 0:
            form = LCLForm(request.POST)
            
        else:
            lcl = LCL.objects.get(pk=id)
            form = LCLForm(request.POST, instance=lcl)
            
        if form.is_valid():
            form = form.save(commit=False)
            user_id = request.user.pk
            form.username = User.objects.get(pk=user_id)
            form.LCL_origin = request.POST['origin']
            form.LCL_chk_date = request.POST['chk_date']
            form.LCL_dest = request.POST['destination']
            form.LCL_ofc = request.POST['ofc'] + request.POST['ofcunit']
            form.save()
            
            
            
        return redirect('/main/LCL_list.html')
    

@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def LCL_delete(request, id):
    lcl = LCL.objects.get(pk=id)
    lcl.delete()
    return redirect('/main/LCL_list.html')

#############################################################################################


def error(request):
    return render(request, 'employee_register/404.html')


def blank(request):
    return render(request, 'employee_register/blank.html')


def buttons(request):
    return render(request, 'employee_register/buttons.html')


def cards(request):
    return render(request, 'employee_register/cards.html')


def charts(request):
    return render(request, 'employee_register/charts.html')


def forgotpassword(request):
    return render(request, 'employee_register/forgot-password.html')


def index(request):
    return render(request, 'employee_register/index.html')


def register(request):
    return render(request, 'employee_register/register.html')


def table(request):
    return render(request, 'employee_register/table.html')


def utilitiesanimation(request):
    return render(request, 'employee_register/utilities-animation.html')


def utilitiesborder(request):
    return render(request, 'employee_register/utilities-border.html')


def utilitiescolor(request):
    return render(request, 'employee_register/utilities-color.html')


def utilitiesother(request):
    return render(request, 'employee_register/utilities-other.html')

def search(request):
    qs = Employee.objects.all()
    q = request.GET.get('q', '')  # q가 없으면 빈 문자열 리턴

    if q:
        qs = qs.filter(dest__icontains=q) | qs.filter(origin__icontains=q) | qs.filter(
            carrier__icontains=q) | qs.filter(position__icontains=q)

    return render(request, 'employee_register/search.html', {
        'employee_list': qs,
        'q': q,

    })


def searchair(request):
    qs = Airfreight.objects.all()
    q = request.GET.get('q', '')  # q가 없으면 빈 문자열 리턴

    if q:
        qs = qs.filter(air_consol__icontains=q) | qs.filter(air_pic__icontains=q) | qs.filter(air_origin__icontains=q)\
            | qs.filter(air_dest__icontains=q)

    return render(request, 'employee_register/searchair.html', {
        'airfreight_list': qs,
        'q': q,

    })


def searchlcl(request):
    qs = LCL.objects.all()
    q = request.GET.get('q', '')  # q가 없으면 빈 문자열 리턴

    if q:
        qs = qs.filter(LCL_pic_code__icontains=q) | qs.filter(LCL_origin__icontains=q) | qs.filter(LCL_dest__icontains=q)\
            | qs.filter(LCL_consol__icontains=q)

    return render(request, 'employee_register/searchlcl.html', {
        'lcl_list': qs,
        'q': q,

    })

    ###################################################################################################################################
