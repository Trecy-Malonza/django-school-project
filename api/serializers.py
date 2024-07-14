# from rest_framework import serializers
# from student.models import Student
# from class.models import SchoolClass


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Student
#         fields="__all__"

# class ClassSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =SchoolClass
#         fields ="__all__"
# serializers.py

from rest_framework import serializers
from student.models import Student
# from schoolclass.models import SchoolClass 
from teacher.models import Teacher
from course.models import Course
from classperiod.models import ClassPeriod

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

# class SchoolClassSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SchoolClass  
#         fields = "__all__"


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
