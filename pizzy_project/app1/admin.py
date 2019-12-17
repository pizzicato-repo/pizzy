from django.contrib import admin

from .models import Teatcher, Student

class TeatcherAdmin(admin.ModelAdmin):
    model = Teatcher



# class StudentAdmin(admin.ModelAdmin):
#     model = Student


admin.site.register(Teatcher, TeatcherAdmin)