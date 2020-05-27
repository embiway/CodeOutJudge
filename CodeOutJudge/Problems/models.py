from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Problem(models.Model):    
    problem_name = models.TextField(max_length=50 , default="NONE")
    problem_statement = models.TextField(max_length = 10000, blank = False)
    user = models.ManyToManyField(Profile)
    def __str__(self):
        return self.problem_name

class OutputFile(models.Model):
    file_content = models.FileField()
    problem = models.ForeignKey(Problem , on_delete=models.CASCADE , default = None)
    def __str__(self):
        return str(self.id)

class InputFile(models.Model):
    file_content = models.FileField()
    output_file = models.OneToOneField(OutputFile , on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem , on_delete=models.CASCADE , default = None)
    def __str__(self):
        return str(self.id)

class Submission(models.Model):
    submission = models.FileField(upload_to="submissions")
    problem = models.ForeignKey(Problem , on_delete=models.CASCADE , default = None)
    def __str__(self):
        return str(self.id)


