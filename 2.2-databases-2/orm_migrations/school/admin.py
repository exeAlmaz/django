from django.contrib import admin

from .models import Student, Teacher

class StudentInline(admin.TabularInline):
    model = Student.teachers.through
    extra = 1

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
    search_fields = ('name', 'subject')
    inlines = [StudentInline]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')
    search_fields = ('name', 'group')
    filter_horizontal = ('teachers',)



