from django.shortcuts import render, redirect
from staff.models import StaffInfo
from student.models import StudentHomework, StudentReminder
from django.contrib.auth.models import User, Group

def add_student(request):
    if request.method == 'POST':
        std_name = request.POST['std_name']
        std_reg_no = request.POST['std_reg_no']
        std_dept = request.POST['std_dept']
        std_sem = request.POST['std_sem']
        std_email = request.POST['std_email']
        std_PhoneNo = request.POST['std_PhoneNo']
        print(std_name, std_reg_no, std_dept, std_sem, std_email, std_PhoneNo)
        return render(request, 'manegment/add_student.html', {'message': 'Student added successfully!'})
    return render(request, 'manegment/add_student.html')

def add_staff(request):
    if request.method == 'POST':
        staff_name = request.POST['staff_name']
        pswd = request.POST['password']
        staff_id = request.POST['staff_id']
        staff_dept = request.POST['dept']
        staff_email = request.POST['email']
        staff_PhoneNo = request.POST['phone_no']
        staff_designation = request.POST['designation']

        new_staff = StaffInfo(staff_id, staff_name, staff_dept, staff_designation, staff_email, staff_PhoneNo)
        newuser = User.objects.create_user(username=staff_id, password=pswd, email=staff_email) 
        usergroup = Group.objects.get(name='staff')

        newuser.save()
        usergroup.user_set.add(newuser)
        new_staff.save()
        
        new_staff.save()

        return redirect('home')
    
    return render(request, 'manegment/add_staff.html')

def send_hw(request):
    if request.method == 'POST':
        hw_title = request.POST['hw_title']
        hw_desc = request.POST['hw_content']
        hw_sem = request.POST['hw_sem']
        hw_author = request.user.username
        hw_dept = request.POST['hw_dept']

        homework = StudentHomework(hw_title=hw_title, hw_desc=hw_desc, hw_author=hw_author, hw_dept=hw_dept, hw_sem=hw_sem)
        homework.save()
        return redirect('send-hw')
    return render(request, 'staff/send_homework.html')

def send_reminder(request):
    print(request.method)
    if request.method == 'POST':
        rmdr_title = request.POST['hw_title']
        rmdr_desc = request.POST['hw_content']
        rmdr_author = request.user.username
        rmdr_std_reg_no = request.POST['reg_no']

        print(rmdr_title, rmdr_desc, rmdr_author, rmdr_std_reg_no)

        reminder = StudentReminder(rmdr_title=rmdr_title, rmdr_desc=rmdr_desc, rmdr_author=rmdr_author, std_reg_no = rmdr_std_reg_no)
        reminder.save()
        return redirect('send-rmdr')
    return render(request, 'staff/send_alerts.html')