from django.urls import path
from . import views

urlpatterns = [
    path('add-class', views.add_class, name='index'),
    path('attendence/<int:key>/<int:card_id>', views.attend, name='index')
]
