from django.contrib import admin
from .models import Student

class StudentListAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'std_class', 'mobile_number', 'gender', 'age']

# Register your models here.
admin.site.register(Student, StudentListAdmin)

