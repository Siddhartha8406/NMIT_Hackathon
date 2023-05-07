from django.urls import path
from . import views

urlpatterns = [
    path('add-student', views.add_student, name='add-student'),
    path('add-staff', views.add_staff, name='add-staff'),
    path('send-hw', views.send_hw, name='send-hw'),
    path('send-rmdr', views.send_reminder, name='send-rmdr'),
]