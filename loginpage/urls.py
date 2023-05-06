from django.contrib import admin
from django.urls import path, include
from loginpage import views

urlpatterns = [
    path("", views.index, name='Login Page'),
    path("signup", views.signup, name='Sign Up Page'),
    path("hhome", views.hhome, name='Home Page'),
    path("dhome", views.dhome, name='Home Page'),
    path("refferal", views.refferal, name='Refferal Page'),
    path("history", views.history, name='History Page'),
    path("thistory", views.thistory, name='''Today's History Page'''),
    path("dhistory", views.dhistory, name='History Page')

]
