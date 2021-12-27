from django.db import models

# Create your models here.
class Students(models.Model):
      GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
      )
      student_reg =models.BigIntegerField(primary_key=True)
      first_name =models.CharField(max_length=64)
      last_name =models.CharField(max_length=64)
      email = models.CharField(max_length=64)
    # email = (User on_delete=     
      profile = models.ImageField(max_length=64,upload_to="student_profile")
      gender =models.CharField(max_length=1, choices=GENDER_CHOICES)
      date_of_birth =models.CharField(max_length=64)
      national_id = models.CharField(max_length=64)
      year_academic =models.CharField(max_length=64)
      department =  models.CharField(max_length=64)
      
      def __int__(self):
        return self.student_reg
    
      class Meta:
          app_label='adminpanel'
          
class Themarks(models.Model):
    student_name=models.CharField(max_length=64)
    student_reg=models.ForeignKey(Students,on_delete=models.CASCADE)
    academic_year= models.CharField(max_length=200)
    module_name=models.CharField(max_length=200)
    module_code=models.CharField(max_length=200)
    module_credits=models.CharField(max_length=200)
    module_marks =models.CharField(max_length=200)
    module_semester=models.CharField(max_length=200)
    module_grade=models.CharField(max_length=200)
    level=models.IntegerField()
    
    def __int__(self):
        return self.student_reg
    
    class Meta:
          app_label='adminpanel'
          
