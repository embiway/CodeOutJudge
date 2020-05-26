from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class OutputFile(models.Model):
    file_content = models.FileField()
    def __str__(self):
        return self.id

class InputFile(models.Model):
    file_content = models.FileField()
    output_file = models.OneToOneField(OutputFile , on_delete=models.CASCADE)
    def __str__(self):
        return self.id

class Submission(models.Model):
    submission = models.FileField()
    def __str__(self):
        return self.id

class Problem(models.Model):
    problem_statement = models.TextField(max_length = 10000, blank = False)
    input_file = models.ForeignKey(InputFile , on_delete=models.CASCADE)
    output_file = models.ForeignKey(OutputFile , on_delete=models.CASCADE)
    def __str__(self):
        return self.id

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    problems = models.ForeignKey(Problem , on_delete=models.CASCADE , null=True)
    submissions = models.ForeignKey(Submission , on_delete=models.CASCADE , null=True)

    def __str__(self):
        return self.user.username

