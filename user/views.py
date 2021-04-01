from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import StudentRegistrationForm, TeacherRegistrationForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import User
User = get_user_model()



def sregister(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if email.find("thapar.edu") == -1:
                messages.add_message(request, messages.INFO, f'''Please enter thapar's email id''')
                return redirect('register')    
            else:
                user = form.save()
                user.is_student = True
                user.save()
                return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'user/register.html', {'form': form})

def tregister(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_teacher = True
            user.save()
            return redirect('login')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'user/register.html', {'form': form})