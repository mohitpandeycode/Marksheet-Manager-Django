from django.contrib import admin
from .models import Student,StudentId,Department,Subject,SubjectMarks

# Register your models here.
admin.site.register(Student)
admin.site.register(StudentId)
admin.site.register(Subject)
admin.site.register(Department)

class subjectmarkadmin(admin.ModelAdmin):
    list_display = ['student','subject','marks']
admin.site.register(SubjectMarks,subjectmarkadmin)