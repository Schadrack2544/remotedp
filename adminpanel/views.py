from django.shortcuts import render

# Create your views here.
def add_Student(request):
    return render(request, 'add_student.html')

    