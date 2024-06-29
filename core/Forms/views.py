from django.shortcuts import render, redirect
from .models import *
#import stripe
# Create your views here.

def Home(request):
    if request.method == "POST":
        data = request.POST
        
        student_name = data.get('student_name')
        student_gender = data.get('student_gender')
        student_phone_No = data.get('student_phone_No')
        student_gmail = data.get('student_gmail')
        student_image = request.FILES.get('student_image')
        student_address = data.get('student_address')
        
        
        """ 
        print(student_name)
        print(student_gender)
        print(student_phone_No)
        print(student_gmail)
        print(student_image)
        print(student_address)
        """
        
        Students.objects.create(
            student_name = student_name,
            student_gender = student_gender,
            student_phone_No = student_phone_No,
            student_gmail = student_gmail,
            student_image = student_image,
            student_address = student_address,
            )
        
        return redirect('/home/')
    
    """
    queryset = Students.objects.all()
    context = {'Students': queryset}
    """
    context = {'amount' : 500}    
    return render(request, "index.html", context)