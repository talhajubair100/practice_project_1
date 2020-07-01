from django.shortcuts import render
from .models import Student


def student_list(request):
    student = Student.objects.all()
    context = {'std_list': student}
    return render(request, 'student/student_list.html', context)


def student_details(request, id):
    details_obj = Student.objects.get(id=id)
    context = {'std_details': details_obj}
    return render(request, 'student/student_details.html', context)