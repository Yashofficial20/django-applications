from django.db import models

# Create your models here.


class Students(models.Model):
    student_name = models.CharField(max_length = 100)
    student_gender = models.CharField(max_length=6, default='Unknown')  
    student_phone_No = models.IntegerField(default=100)
    student_gmail = models.EmailField()
    student_image = models.ImageField(upload_to = "pics", null = True)
    student_address = models.TextField()
    