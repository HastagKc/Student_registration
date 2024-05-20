from django.shortcuts import render,redirect
from django.http import HttpResponse
# import model 
from .models import Student
# import message 
from django.contrib import messages

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        name = request.POST['name']
        roll = request.POST['roll']
        email = request.POST['email']
        password = request.POST['password']

        stu = Student(name=name, roll=roll, email=email, password=password)
        stu.save()
        messages.success(request, 'Submit Successfully')
        
        # After saving, redirect to the same page to display the form and data
        return redirect('home')
    
    else:
        stu_data = Student.objects.all()
        context = {'stu_data': stu_data}
        
    return render(request, 'curd_app/home.html', context)


def delete(request,id):
    std_data = Student.objects.get(id=id)
    std_data.delete()
    messages.success(request, 'Deleted Successfully')
    return redirect('home')


def update(request):
    return render(request,'curd_app/update.html')