from django.db import models

class login_details(models.Model):
    user_type = [
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('store', 'Store')
    ]
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=30)
    user_type = models.CharField(max_length=7, choices=user_type, default='student')