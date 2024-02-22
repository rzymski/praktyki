from django.urls import path

from . import views

urlpatterns = [
    path("", views.indexView, name="index"),
    path("studentlist/", views.studentsList, name="studentsList"),
    path("student/<str:index>", views.studentDetail, name="studentDetail"),

    path("teacherlist/", views.teachersList, name="teachersList"),
    path("teacher/<str:index>", views.teacherDetail, name="teacherDetail"),

    path("grades/", views.gradesList, name="gradesList"),

    path("test/<str:index>", views.testViewWithIndex, name="test"),
    path("test/", views.testView, name="test"),
]
