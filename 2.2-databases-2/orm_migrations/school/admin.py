from django.contrib import admin

from .models import Student, Teacher

# class StudentTeacherInline(admin.TabularInline):
#     model = Student
#     extra = 3
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name']
    # inlines = [StudentTeacherInline, ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name']
