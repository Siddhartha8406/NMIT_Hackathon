from django.db import models

class StudentInfo(models.Model):
    depts = [
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('AT', 'Automobile Engineering'),
    ]
    sems = [
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th'),
        ('5', '5th'),
        ('6', '6th'),
    ]

    std_name = models.CharField(max_length=50)
    std_reg_no = models.CharField(max_length=50, primary_key=True)
    std_dept = models.CharField(max_length=3, choices=depts)
    std_sem = models.CharField(max_length=1, choices=sems)
    std_email = models.CharField(max_length=50, unique=True)
    std_PhoneNo = models.CharField(max_length=10, unique=True)
    std_class_attended = models.IntegerField(default=0)

class StudentHomework(models.Model):
    depts = [
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('AT', 'Automobile Engineering'),
    ]
    sems = [
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th'),
        ('5', '5th'),
        ('6', '6th'),
    ]
    hw_id = models.AutoField(primary_key=True)
    hw_title = models.CharField(max_length=50)
    hw_desc = models.CharField(max_length=500)
    hw_author = models.CharField(max_length=50)
    hw_dept = models.CharField(max_length=3, choices=depts)
    hw_sem = models.CharField(max_length=1, choices=sems)
    hw_date = models.DateField(auto_now=True)

class StudentReminder(models.Model):
    rmdr_id = models.AutoField(primary_key=True)
    rmdr_title = models.CharField(max_length=50)
    rmdr_desc = models.CharField(max_length=500)
    rmdr_author = models.CharField(max_length=50)
    std_reg_no = models.CharField(max_length=50)
    hw_date = models.DateField(auto_now=True)