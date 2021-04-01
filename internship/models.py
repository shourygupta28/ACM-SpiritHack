from django.db import models
from django.urls import reverse
from user.models import User
from markdown_deux import markdown
from django.utils.safestring import mark_safe
from phonenumber_field.modelfields import PhoneNumberField

class StudentInternship(models.Model):
    user = models.ForeignKey(User, limit_choices_to={'is_student': True}, on_delete=models.CASCADE, null=True)
    startup = models.CharField(max_length=100, default='')
    duration = models.CharField(max_length=20)
    stipend = models.CharField(max_length=100)
    apply_by = models.DateField(default='2000-01-01', help_text='YYYY-MM-DD Format should be followed for the date.')
    link = models.URLField(default='', help_text='Add link for application. ')
    visibility = models.BooleanField(default=False)


    def __str__(self):
        return self.startup

    def get_absolute_url(self):
        return reverse('internship-detail', kwargs={'pk' : self.pk})


class Project(models.Model):
    project = models.CharField(max_length=100, default='')
    field_of_project = models.CharField(max_length=100, default='')
    duration = models.CharField(max_length=20)
    about = models.TextField()
    location = models.CharField(max_length=100)
    stipend = models.CharField(max_length=100)
    skills_required = models.CharField(max_length=500)
    no_of_vaccancy = models.PositiveIntegerField()
    perks = models.CharField(max_length=100)
    apply_by = models.DateField(default='2000-01-01', help_text='YYYY-MM-DD Format should be followed for the date.')

    def __str__(self):
        return self.project



class InternshipApplication(models.Model):
    internship = models.ForeignKey(Project, on_delete=models.CASCADE, default='', related_name='internship')
    message = models.TextField(max_length = 1200, blank=True, default='')
    resume = models.URLField(default='', help_text='Add the drive link to your resume.')
    applied_by = models.ForeignKey(User, on_delete=models.CASCADE, default='', related_name='intern')
    
    def __str__(self):
        return self.internship.project + "(" + str(self.internship.id) + ")" + " - " + self.applied_by.name

    def message_markdown(self):
        message = self.message
        return mark_safe(markdown(message))