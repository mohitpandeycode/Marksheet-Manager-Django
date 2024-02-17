from django.shortcuts import render,HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q,Sum
from .models import *

# Create your views here.
def index(request):
    queryset = Student.objects.all()

    if request.method == "GET":
        search = request.GET.get('search')
        if search != None:
            queryset = Student.objects.filter(
                Q(student_name__icontains = search)|
                Q(student_id__student_id__icontains = search)|
                Q(department__department__icontains = search)|
                Q(student_email__icontains = search)|
                Q(student_age__icontains = search)
                )
            
    paginator = Paginator(queryset, 20) 
    page_number = request.GET.get('page')
    final_Data = paginator.get_page(page_number)
    total_page = final_Data.paginator.num_pages

    data={
        'info':final_Data,
        'lastpage':total_page,
        'pagelist':[n+1 for n in range(total_page)]
}


    return render(request,'index.html',data)

def Marks(request,student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    totalmarks = queryset.aggregate(totalmarks = Sum('marks')) 
    first_subject_mark = queryset.first()
    student_name = first_subject_mark.student.student_name
    branch = first_subject_mark.student.department.department
    email = first_subject_mark.student.student_email
    age = first_subject_mark.student.student_age

    rank = totalmarks['totalmarks']
    new_rank = 0
    if rank<350 and rank >=190:
        new_rank = "Second Division..."
    elif rank>=350 and rank<500:
        new_rank = "First Division..."
    elif rank>=500:
        new_rank = "Top Rank('Marit')..."
    else:
        new_rank = "Fail..!"

    data = {'queryset':queryset,'totalmarks':totalmarks,'newrank':new_rank,'student_name':student_name,'branch':branch,'email':email,'age':age}
    return render(request,'Marks.html',data)