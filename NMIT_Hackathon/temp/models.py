from django.db import models

class TotalClasses(models.Model):
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

    sem = models.CharField(max_length=1, choices=sems)
    dept = models.CharField(max_length=3, choices=depts)
    total_classes = models.IntegerField(default=0)