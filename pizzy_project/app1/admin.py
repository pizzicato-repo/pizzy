from django.contrib import admin

from .models import Teatcher, Student, Discipline

class TeatcherAdmin(admin.ModelAdmin):
    model = Teatcher

class DisciplineAdmin(admin.ModelAdmin):
    model = Discipline


# class StudentAdmin(admin.ModelAdmin):
#     model = Student


admin.site.register(Teatcher, TeatcherAdmin)
admin.site.register(Discipline, DisciplineAdmin)