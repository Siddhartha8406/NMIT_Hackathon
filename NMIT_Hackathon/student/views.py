from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .models import StudentInfo, StudentHomework, StudentReminder
from staff.models import StaffInfo

def create_student(request):
    name = request.POST['username']
    pswd = request.POST['password']
    acc_type = request.POST['group']
    reg_no = request.POST['reg']
    dept = request.POST['dept']
    sem = request.POST['sem']
    mail = request.POST['email']
    phone_no = request.POST['phone_no']
    print(dept)

    std = StudentInfo(std_name=name, std_reg_no=reg_no, std_dept=dept, std_sem=sem, std_email=mail)
    user = User.objects.create_user(username=reg_no, password=pswd, email=mail)
    usergroup = Group.objects.get(name=acc_type)

    usergroup.user_set.add(user)
    user.save()
    std.save()
    return redirect('index')

def homework(request):
    if request.user.is_authenticated:
        print(request.user.groups.all()[0].name)
        if request.user.groups.all()[0].name == 'student':
            student_data = StudentInfo.objects.get(std_reg_no=request.user.username)
            student = list(StudentHomework.objects.all().values().filter(hw_dept=student_data.std_dept, hw_sem=student_data.std_sem))
            return render(request, 'student/homework.html', {'homeworks': student})
        elif request.user.groups.all()[0].name == 'staff':
            hw = list(StudentHomework.objects.all().values())
            return render(request, 'staff/homework.html', {'homeworks': hw})
    else:
        return redirect('index')

def contact_teachers(request):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'student':
            staff = list(StaffInfo.objects.all().values())
            print(staff)
            print(type(staff))
            return render(request, 'student/contact_teachers.html', {'user': staff})
        else:
            return redirect('home')
    return render(request, 'student/contact_teachers.html')

def alert(request):
    if request.user.is_authenticated:
        print(request.user.groups.all()[0].name)
        if request.user.groups.all()[0].name == 'student':
            alert_data = StudentReminder.objects.get(std_reg_no=request.user.username)
            student = list(StudentReminder.objects.all().values().filter(std_reg_no = request.user.username))
            return render(request, 'student/alerts.html', {'alerts': student})
        else:
            return redirect('home')
    else:
        return redirect('index')
