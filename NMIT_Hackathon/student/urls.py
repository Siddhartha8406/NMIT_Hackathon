from django.urls import path
from . import views

urlpatterns = [
    path('add_std', views.create_student, name='add_student'),
    path('homework', views.homework, name='homework'),
    path('alert', views.alert, name='alert'),
    path('contact_teachers', views.contact_teachers, name='contact_teachers'),
]