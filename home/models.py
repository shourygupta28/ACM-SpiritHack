from django.db import models

class YrBranch(models.Model):
    year                        = models.IntegerField(default=0, null=True)
    branch                      = models.CharField(default='', max_length=50, null=True)

    def __str__(self):
        return str(self.year) + "_" + str(self.branch)

class Subject(models.Model):
    subject_code 				= models.CharField(unique=True, max_length=10)
    subject_name                = models.CharField(default='', max_length=100)
    yr_branch                   = models.ManyToManyField(YrBranch)
    visibilty                   = models.BooleanField(default=True)

    def __str__(self):
        return self.subject_code

