from django.contrib import admin
from .models import Users, Departments, Interests

# Register your models here.
admin.site.register(Users)
admin.site.register(Departments)
admin.site.register(Interests)