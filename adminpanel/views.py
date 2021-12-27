from django.core.checks import messages
from django.shortcuts import redirect, render
from Academic.models import Marks, Student
# Create your views here.
def add_Student_Mark(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_reg = request.POST.get('student_reg')
        academic_year= request.POST.get('academic_year')
        module_name = request.POST.get('module_name')
        module_code = request.POST.get('module_code')
        module_credits = request.POST.get('module_credits')
        module_semester = request.POST.get('module_semester')
        level_name = request.POST.get('level_name')
        
        
        marks=Marks()
        marks.create(student_name=student_name,student_reg=student_reg,academic_year=academic_year,module_name=module_name,module_code=module_code,module_credits=module_credits,module_semester=module_semester,level_name=level_name)
        
     
        
    return render(request, 'add_student.html')

def add_student(request):
    if request.method == 'POST':
        student_reg =request.POST.get('student_reg')
        first_name =request.POST.get('first_name')
        last_name =request.POST.get('last_name')
        email = request.POST.get('email')
        # email = (User on_delete=     
        profile = request.POST.get('profile')
        gender =request.POST.get('gender')
        date_of_birth =request.POST.get('date_of_birth')
        national_id = request.POST.get('national_id')
        year_academic = request.POST.get('year_academic')
        department =  request.POST.get('department')
        
        stud=Student()
        stud.create(email=email,national_id=national_id,first_name=first_name,last_name=last_name,student_reg=student_reg,department=department,date_of_birth=date_of_birth,profile=profile,gender=gender,year_academic=year_academic)
        stud.save()
        messages.info("Successfully Added student")
        return redirect('addstudents')
    else:
        return render(request, 'addstudent.html')    
def index(request):
        return render(request,'adminpanel/index.html',)