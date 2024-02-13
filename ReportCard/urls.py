from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('marks/<student_id>/',views.Marks,name='marks')
]