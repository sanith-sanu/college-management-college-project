from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path,include
from .import views







urlpatterns = [
   path('',views.index,name='index'),
   path('log_in',views.log_in,name='log_in'),
   path('admin_home',views.admin_home,name='admin_home'),
   path('teacher_home',views.teacher_home,name='teacher_home'),
   path('log_out',views.log_out,name='log_out'),
   path('teacher_signup',views.teacher_signup,name='teacher_signup'),
   path('add_course',views.add_course,name='add_course'),
   path('add_stud',views.add_stud,name='add_stud'),
   path('addc',views.addc,name='addc'),
   path('adds',views.adds,name='adds'),
   path('addt',views.addt,name='addt'),
   path('display_teacher',views.display_teacher,name='display_teacher'),
   path('delete/<int:pk>',views.delete,name='delete'),
   path('show',views.show,name='show'),
   path('update_stud/<int:pk>',views.update_stud,name='update_stud'),
   path('delete_stud/<int:pk>',views.delete_stud,name='delete_stud'),
   path('edit_stud/<int:pk>',views.edit_stud,name='edit_stud'),
   path('display',views.display,name='display'),
   path('updatetea',views.updatetea,name='updatetea'),
  
  
]
