from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics" , null = True)

    def __str__(self):
        return self.user.username

class Problem(models.Model):    
    problem_name = models.TextField(max_length=50 , default="NONE")
    problem_statement = models.TextField(max_length = 10000, blank = False)
    input_info = models.TextField(max_length = 10000 , null = True)
    output_info = models.TextField(max_length = 10000 , null = True)
    constraints = models.TextField(max_length = 10000 , null = True)

    time_limit = models.FloatField(default = 1.0000)
    memory_limit = models.IntegerField(default = 256000)
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
    time = models.TextField(max_length=20 , default = "0.0000000" , null = True)
    memory = models.IntegerField(null=True , default=0)
    status = models.TextField(max_length = 100 , default = "Unchecked" , null=True)
    problem = models.ForeignKey(Problem , on_delete=models.CASCADE , default = None)
    user = models.ForeignKey(Profile , on_delete=models.CASCADE , null=True)
    def __str__(self):
        return str(self.id)


