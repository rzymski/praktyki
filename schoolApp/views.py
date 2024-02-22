from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import *
from .functions import *
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Q, IntegerField, F, ExpressionWrapper
from .decorators import *


def indexView(request):
    return render(request, 'main/index.html')


@combinedCheckTimeAndSqlDecorator
@login_required(login_url='login')
def studentsList(request):
    students = getAllStudentsMainDataInList()
    return render(request, 'main/studentsList.html', {"students": students})


@combinedCheckTimeAndSqlDecorator
@login_required(login_url='login')
def studentDetail(request, index):
    studentData = getStudentAllData(index)
    return render(request, 'main/studentDetail.html', studentData)


@combinedCheckTimeAndSqlDecorator
@login_required(login_url='login')
def teachersList(request):
    teachers = Teacher.objects.annotate(
        averageGrade=Avg('id__gradesubjectleader__grade__gradeValue'),
        countGrade=Count('id__gradesubjectleader__grade')
    ).prefetch_related("id")
    # for teacher in teachers:
    #     ic(teacher.name, teacher.surname, teacher.averageGrade, teacher.countGrade)
    return render(request, 'main/teachersList.html', {"teachers": teachers})


@combinedCheckTimeAndSqlDecorator
@login_required(login_url='login')
def teacherDetail(request, index):
    teacherData = getTeacherAllData(index)
    return render(request, 'main/teacherDetail.html', teacherData)


@combinedCheckTimeAndSqlDecorator
@login_required(login_url='login')
def gradesList(request):
    resultList = (GradeSubjectLeader.objects
    .annotate(semesterOddAndEven=ExpressionWrapper(F('grade__semester') % 2, output_field=IntegerField()))
    .values(
        'subject__name',
        'leader__id',
        'leader__teacher__name',
        'leader__teacher__surname',
        'leader__teachergroup__id_teacher1__name',
        'leader__teachergroup__id_teacher1__surname',
        'leader__teachergroup__id_teacher2__name',
        'leader__teachergroup__id_teacher2__surname',
        'leader__teachergroup__id_teacher3__name',
        'leader__teachergroup__id_teacher3__surname',
        'leader__teachergroup__id_teacher4__name',
        'leader__teachergroup__id_teacher4__surname',
        'semesterOddAndEven',
    )
    .annotate(
        grade1Count=Count('grade__gradeValue', filter=Q(grade__gradeValue=1)),
        grade2Count=Count('grade__gradeValue', filter=Q(grade__gradeValue=2)),
        grade3Count=Count('grade__gradeValue', filter=Q(grade__gradeValue=3)),
        grade4Count=Count('grade__gradeValue', filter=Q(grade__gradeValue=4)),
        grade5Count=Count('grade__gradeValue', filter=Q(grade__gradeValue=5)),
        grade6Count=Count('grade__gradeValue', filter=Q(grade__gradeValue=6)),
        averageGrade=Avg('grade__gradeValue'),
    ))
    return render(request, 'main/gradesList.html', {"grades": resultList})




@combinedCheckTimeAndSqlDecorator
def testView(request):
    ic("Funkcja")
    return render(request, 'test/test.html')


def testViewWithIndex(request, index):
    student = getStudentAllData(index)
    return render(request, 'test/test.html', student)
