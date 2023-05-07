from django.shortcuts import render, redirect
from student.models import StudentInfo
from staff.models import StaffInfo
from temp.models import TotalClasses
from django.contrib.auth import logout

def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'index.html')

def home(request):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'student':
            student = StudentInfo.objects.get(std_email=request.user.email)

            classes_attended = TotalClasses.objects.get(dept=student.std_dept, sem=student.std_sem).total_classes
            return render(request, 'student/index.html', {'user': student, 'taken':classes_attended})
        elif request.user.groups.all()[0].name == 'staff':
            print('Staff')
            staff = StaffInfo.objects.get(staff_email=request.user.email)
            return render(request, 'staff/index.html', {'user': staff})
    else:
        return redirect('index')

def logout_user(request):
    logout(request)
    return redirect('index')