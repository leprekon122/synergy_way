from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.FirstPage.as_view(), name='first_page'),
    path('Second_page', views.SecondPage.as_view(), name="second_page"),
    path('update/<int:pk>', views.CreateUserUpdate.as_view(), name='user_update'),
    path('update_group/<int:pk>', views.CreateGroupUpdate.as_view(), name='update_group')
]
