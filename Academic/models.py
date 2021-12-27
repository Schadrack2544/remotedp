from django.contrib.auth.models import User
from django.db import models


class College(models.Model):
    college_code = models.CharField(max_length=10, primary_key=True)
    college_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default="Nyarugenge")

    def __str__(self):
        return self.college_code

    class Meta:
        app_label = 'Academic'


class School(models.Model):
    college_code = models.ForeignKey(College, on_delete=models.CASCADE, related_name="set_college")
    school_code = models.CharField(max_length=10, primary_key=True)
    school_name = models.CharField(max_length=100)

    def __str__(self):
        return self.school_code

    class Meta:
        app_label = 'Academic'


class Level(models.Model):
    level_code = models.CharField(max_length=10, primary_key=True)
    level_name = models.CharField(max_length=50)

    def __str__(self):
        return self.level_name

    class Meta:
        app_label = 'Academic'


class Academic_year(models.Model):
    academic_list = models.CharField(max_length=16, primary_key=True)
    academic_comment = models.TextField(max_length=1083)


    def __str__(self):
        return self.academic_list

    class Meta:
        app_label = 'Academic'


class Department(models.Model):
    school_code = models.ForeignKey(School, on_delete=models.CASCADE)
    department_code = models.CharField(max_length=10, primary_key=True)
    department_name = models.CharField(max_length=100)
    academic_year = models.ForeignKey(Academic_year, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name

    class Meta:
        app_label = 'Academic'


class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    student_reg = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    # email = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to="student_profile")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    national_id = models.PositiveBigIntegerField()
    year_academic = models.ForeignKey(Academic_year, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __int__(self):
        return self.student_reg

    class Meta:
        app_label = 'Academic'


class Semester(models.Model):
    semester_code = models.CharField(max_length=8, primary_key=True)
    semester_name = models.CharField(max_length=24)

    def __str__(self):
        return self.semester_name

    class Meta:
        app_label = 'Academic'


class Lecturer(models.Model):
    email = models.EmailField(max_length=255, primary_key=True)
    lecturer_name = models.CharField(max_length=255)
    academic_year = models.ForeignKey(Academic_year, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.lecturer_name

    class Meta:
        app_label = 'Academic'


class Credit(models.Model):
    module_credits = models.CharField(max_length=255, default="10")

    def __int__(self):
        return self.module_credits


class Module(models.Model):
    module_code = models.CharField(max_length=10, primary_key=True)
    module_name = models.CharField(max_length=100)
    credits = models.ForeignKey(Credit, on_delete=models.CASCADE, default='10')
    module_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='set_for_module')
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.module_code

    class Meta:
        app_label = 'Academic'


class Marks(models.Model):
    student_reg = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="set_student_mark")
    module_code = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="set_module_code")
    module_name = models.CharField(max_length=100)
    marks = models.IntegerField()
    grade = models.CharField(max_length=1)
    semester_marks = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='semester_marks', default=0)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='level_marks', default='level 1')


    class Meta:
        app_label = 'Academic'


class Transcript(models.Model):
    transcript_code = models.CharField(max_length=10, primary_key=True)
    student_reg = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="set_student_reg")
    student_Fname = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="set_student_fname")
    student_Lname = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="set_student_lname")
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="set_module_id")
    level_year = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="set_level_year")
    student_profile = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="set_student_profile")
    dob = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="set_dob")
    marks = models.ForeignKey(Marks, on_delete=models.CASCADE, related_name="set_marks")
    grade = models.ForeignKey(Marks, on_delete=models.CASCADE, related_name="set_grade")
    credits = models.IntegerField()

    def __str__(self):
        return self.transcript_code

    class Meta:
        app_label = 'Academic'
class Payment(models.Model):
    payment_invoice_number=models.CharField(max_length=255,primary_key=True)
    student_reg = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="studen_reg_number")
    amount_due = models.IntegerField(default=5000)
    level = models.CharField(max_length=10)
    is_paid = models.BooleanField(default=True)
    
    
class payment_Order(models.Model):
    txn_id = models.CharField(max_length=12,primary_key=True)
    student_reg=models.ForeignKey(Student, on_delete=models.CASCADE)
    payment_invoice_number = models.ForeignKey(Payment, on_delete=models.CASCADE)