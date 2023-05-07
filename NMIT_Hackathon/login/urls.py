from django.urls import path
from . import views
from main.views import index

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('SignUp', views.signup, name='signup'),
    
    path('sign_up', views.sign_up, name='sign_up'),
]
