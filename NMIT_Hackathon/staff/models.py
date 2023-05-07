from django.db import models

class StaffInfo(models.Model):
    depts = [
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('AT', 'Automobile Engineering'),
    ]

    staff_id = models.CharField(max_length=50, primary_key=True)
    staff_name = models.CharField(max_length=50)
    staff_dept = models.CharField(max_length=3, choices=depts)
    staff_designation = models.CharField(max_length=50)
    staff_email = models.CharField(max_length=50, unique=True)
    staff_PhoneNo = models.CharField(max_length=10, unique=True)