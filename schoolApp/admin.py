from django.contrib import admin
from .models import *


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'schoolNumber')


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'school', 'actualClass')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('index', 'pesel', 'name', 'surname', 'schoolClass')


@admin.register(StudentArchive)
class StudentArchiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'index', 'pesel', 'name', 'surname', 'schoolClass')


@admin.register(DetailStudent)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display = ('studentIndex', 'rspo', 'birthDate', 'birthPlace', 'matura', 'osm_gim')


@admin.register(DetailStudentArchive)
class StudentDetailArchiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'studentIndex', 'rspo', 'birthDate', 'birthPlace', 'matura', 'osm_gim')


@admin.register(ExamJunior)
class StudentExamJuniorAdmin(admin.ModelAdmin):
    list_display = ('id', 'index', 'polish', 'mathematics')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'index', 'semester', 'legitimate', 'illegitimate', 'lateAttendance', 'present')


@admin.register(Grade)
class StudentGradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'semester', 'gradeValue', 'student')

