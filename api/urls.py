from django.urls import path
from .views import StudentListView
from .views import TeacherListView
from .views import CourseListView
from .views import ClassPeriodListView
from .views import ClassRoomListView
from .views import StudentDetailView
from .views import TeacherDetailView
from .views import CourseDetailView
from .views import ClassPeriodDetailView
from .views import TeacherAssignmentListView
from .views import TeacherClassAssignmentListView 
from .views import WeeklyTimetableListView


urlpatterns =[
    path("student/",StudentListView.as_view(),name="student_list_view"),
    path("teacher/",TeacherListView.as_view(),name="teacher_list_view"),
    path("course/",CourseListView.as_view(),name="course_list_view"),
    path("classperiod/",ClassPeriodListView.as_view(),name="classperiod_list_view"),
    path("classroom/",ClassRoomListView.as_view(),name="classroom_list_view"),
    path("student/<int:id>/",StudentDetailView.as_view(),name="studentdetail_view"),
    path("teacher/<int:id>/",TeacherDetailView.as_view(),name="teacherdetail_view"),
    path("course/<int:id>/",CourseDetailView.as_view(),name="coursedetail_view"),
    path("classperiod/<int:id>/",ClassPeriodDetailView.as_view(),name="classperioddetail_view"),
    path("teacher/assign-course/", TeacherAssignmentListView.as_view(), name="teacher_assign_course_view"),  
    path("teacher/assign-class/", TeacherClassAssignmentListView.as_view(), name="teacher_assign_class_view"),
    path("timetable/", WeeklyTimetableListView.as_view(), name="weekly_timetable_view"),  

]