from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import ProjectInternshipForm, InternshipForm, ApplicationForm
from .models import *


def InternshipProjects(request):
    internships = Project.objects.all().order_by('-apply_by')
    context = {
        'internships': internships
    }
    return render(request, 'internship/ProjectInternship.html', context)

def Internships(request):
    internships = StudentInternship.objects.filter(visibility = True).order_by('-apply_by')
    context = {
        'internships': internships
    }
    return render(request, 'internship/Internship.html', context)
    
    
def InternshipCreateView(request):
    if request.method == 'POST':
        if request.user.is_student:
            form = InternshipForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(
                    request, 'Your submission has been sent to our team for review.')
        else:
            form = ProjectInternshipForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(
                    request, 'Done!')

        return redirect('internship-opportunities')

    else:
        if request.user.is_student:
            form = InternshipForm()
        else:
            form = ProjectInternshipForm()

    context = {
        'form': form,
    }

    return render(request, 'internship/CreateInternship.html', context)

def apply(request, pk):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.internship = Project.objects.get(id = pk)
            form.instance.applied_by = request.user
            form.save()
            return redirect('project-internships')

    else:
        form = ApplicationForm()

    context = {
        'form': form,
    }

    return render(request, 'internship/ApplyforInternship.html', context)


def check_internship(request):
    if request.user.is_superuser == True:
        internships = StudentInternship.objects.filter(visibility = False)
        context = {
            'internships': internships
        }
        return render(request, 'internship/CheckInternshipVisibility.html', context)
    else:
        internships = StudentInternship.objects.filter(visibility = True)
        context = {
            'internships': internships
        }
        return render(request, 'internship/ProjectInternship.html', context)

def accept(request, pk):
    if request.user.is_superuser == True:
        internship = StudentInternship.objects.get(id=pk)
        internship.visibility = True
        internship.save()
        u = internship.user
        c = u.Coins
        c = c+10
        u.Coins = c
        u.save()
    
    return render(request, 'internship/CheckInternshipVisibility.html') 

