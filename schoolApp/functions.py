from .models import *
from icecream import ic
from django.db.models import Prefetch, Count
from django.db import connection, reset_queries
import time


def measure_execution_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


class StudentAllData:
    def __init__(self, studentId):
        self.student = (Student.objects.filter(index=studentId).select_related("schoolClass", "schoolClass__school", "details")
                        .prefetch_related("examjunior_set", "exam8class_set", "examprofession_set", "matura_set",
                                          "studentarchive_set", "details__detailstudentarchive_set",
                                          Prefetch('attendance_set', queryset=Attendance.objects.all().order_by('semester'), to_attr='attendanceOrderBySemester')).first())
        self.schoolClass = self.student.schoolClass
        self.school = self.schoolClass.school
        self.details = self.student.details
        self.juniorExams = self.student.examjunior_set.all()  # ExamJunior.objects.filter(index=self.student)
        self.class8Exams = self.student.exam8class_set.all()  # Exam8Class.objects.filter(index=self.student)
        self.professionExams = self.student.examprofession_set.all()  # ExamProfession.objects.filter(index=self.student)
        self.maturaExams = self.student.matura_set.all()  # Matura.objects.filter(index=self.student)
        self.attendance = self.student.attendanceOrderBySemester  # Attendance.objects.filter(index=self.student).order_by('semester')
        self.gradesQuery = (Grade.objects.filter(student=self.student).prefetch_related("gradesubjectleader__subject").values('semester', 'gradeValue', 'gradesubjectleader__subject__name')
                            .annotate(count=Count('gradeValue')).order_by('semester', 'gradesubjectleader__subject__name', 'gradeValue'))

        self.studentArchive = self.student.studentarchive_set.all()
        self.detailsArchive = self.details.detailstudentarchive_set.all()
        # ic(self.schoolClass)
        # ic(self.school)
        # ic(self.details)
        # ic(self.juniorExams)
        # ic(self.class8Exams)
        # ic(self.professionExams)
        # ic(self.maturaExams)
        # ic(self.attendance)
        # ic(self.gradesQuery)
        # ic(self.studentArchive)
        # ic(self.detailsArchive)

    def getAllProperties(self):
        return vars(self)


def getStudentAllData(studentId):
    student = StudentAllData(studentId)
    return student.getAllProperties()


class StudentMainData:
    def __init__(self, student):
        self.index = student.index
        self.actualClass = student.schoolClass.actualClass
        self.pesel = student.pesel
        self.name = student.name
        self.surname = student.surname
        self.schoolName = student.schoolClass.school.name


def getStudentMainData(student):
    studentData = StudentMainData(student)
    return studentData


def getAllStudentsMainDataInList():
    students = Student.objects.select_related("schoolClass__school").all()
    studentsListData = []
    for student in students:
        studentData = getStudentMainData(student)
        studentsListData.append(studentData)
    return studentsListData


class TeacherAllData:
    def __init__(self, teacherId):
        self.teacher = Teacher.objects.filter(id=teacherId).select_related("id").first()
        leaderObject = self.teacher.id
        self.gradesBySubject = Subject.objects.filter(
            gradesubjectleader__leader_id=leaderObject.id
        ).values('id', 'name', 'gradesubjectleader__grade__semester', 'gradesubjectleader__grade__gradeValue').annotate(
            grades_count=Count('gradesubjectleader__grade'))
        # for entry in self.gradesBySubject:
        #     subject_id = entry['id']
        #     subject_name = entry['name']
        #     semester = entry['gradesubjectleader__grade__semester']
        #     grade_value = entry['gradesubjectleader__grade__gradeValue']
        #     grades_count = entry['grades_count']
        #     ic(subject_id, subject_name, semester, grade_value, grades_count)

    def getAllProperties(self):
        return vars(self)


def getTeacherAllData(teacherId):
    teacher = TeacherAllData(teacherId)
    return teacher.getAllProperties()
