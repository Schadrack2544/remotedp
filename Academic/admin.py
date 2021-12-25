from django.contrib import admin
from .models import College, School, Department, Semester, Module, Transcript, Lecturer, Academic_year, Level, Credit, \
    Student, Marks


class CollegeAdmin(admin.ModelAdmin):
    list_display = ('college_code', 'college_name', 'location')


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('college_code', 'school_code', 'school_name')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('school_code', 'department_code', 'department_name', 'level')


class LecturerConfig(admin.ModelAdmin):
    list_display = ('email','lecturer_name', 'academic_year', 'school')


class StudentConfig(admin.ModelAdmin):
    list_display = ('student_reg', 'first_name','last_name','email','gender','date_of_birth','national_id','year_academic','department')


class ModuleConfig(admin.ModelAdmin):
    list_display = ('module_code','module_name','credits','module_department','level','semester','lecturer')


class Academic_yearConfig(admin.ModelAdmin):
    list_display = ('academic_list',)


class SemesterConfig(admin.ModelAdmin):
    list_display = ('semester_code','semester_name')


class TranscriptConfig(admin.ModelAdmin):
    list_display = ('transcript_code', 'student_reg', 'student_Fname', 'student_Lname', 'module_id', 'level_year')


class LevelConfig(admin.ModelAdmin):
    list_display = ('level_code', 'level_name')


class CreditConfig(admin.ModelAdmin):
    list_display = ('module_credits',)


class MarksConfig(admin.ModelAdmin):
    list_display = ('module_code','student_reg','marks','grade')


admin.site.register(College, CollegeAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Module, ModuleConfig)
admin.site.register(Academic_year, Academic_yearConfig)
admin.site.register(Semester, SemesterConfig)
admin.site.register(Lecturer, LecturerConfig)
admin.site.register(Student, StudentConfig)
admin.site.register(Transcript, TranscriptConfig)
admin.site.register(Level, LevelConfig)
admin.site.register(Credit, CreditConfig)
admin.site.register(Marks, MarksConfig)

