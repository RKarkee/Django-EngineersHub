from django.contrib import admin
from . models import User,Job,Applicant,EmployeeDetails,Hire,EmployeeProfile
# Register your models here.

admin.site.register(User)
admin.site.register(Job)
admin.site.register(Applicant)
admin.site.register(EmployeeDetails)
admin.site.register(Hire)
admin.site.register(EmployeeProfile)