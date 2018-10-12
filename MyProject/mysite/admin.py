from django.contrib import admin

# Register your models here.
from .models import Student, Contact

admin.site.register(Student)
admin.site.register(Contact)