

from rest_framework import serializers
from student.models import Student
from classroom.models import ClassRoom
from teacher.models import Teacher
from course.models import Course
from classperiod.models import ClassPeriod
from timetable.models import Timetable


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model =ClassRoom
        fields ="__all__"




class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields ="__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model =Course
        fields ="__all__"

class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model =ClassPeriod
        fields ="__all__"


class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields ="__all__"
