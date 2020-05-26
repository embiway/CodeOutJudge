from django.contrib import admin
from .models import Problem , Profile , Submission , InputFile , OutputFile

# Register your models here.

admin.site.register(Profile )
admin.site.register(Problem)
admin.site.register(Submission)
admin.site.register(InputFile)
admin.site.register(OutputFile)
