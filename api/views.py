from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from classroom.models import ClassRoom
from .serializers import ClassRoomSerializer
from student.models import Student
from .serializers import StudentSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
from course.models import Course
from .serializers import CourseSerializer
from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer
from .serializers import TimetableSerializer
from timetable.models import Timetable  

# Create your views here.
class TeacherAssignmentListView(APIView):
    def post(self, request):
        teacher_id = request.data.get("teacher_id")
        course_id = request.data.get("course_id")
        teacher = Teacher.objects.get(id=teacher_id)
        course = Course.objects.get(id=course_id)
        teacher.courses.add(course)
        return Response({"status": "Course assigned to teacher"}, status=status.HTTP_202_ACCEPTED)

class TeacherClassAssignmentListView(APIView):
    def post(self, request):
        teacher_id = request.data.get("teacher_id")
        class_id = request.data.get("class_id")
        teacher = Teacher.objects.get(id=teacher_id)
        classroom = ClassRoom.objects.get(id=class_id)
        teacher.classrooms.add(classroom)
        return Response({"status": "Class assigned to teacher"}, status=status.HTTP_202_ACCEPTED)

class WeeklyTimetableListView(APIView):
    def get(self, request):
        timetable = Timetable.objects.all()
        serializer = TimetableSerializer(timetable, many=True)  
        return Response(serializer.data)

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        country=request.query_params.get("country")
        first_name=request.query_params.get("first_name")
        if country:
            students=students.filter(country=country)
        if first_name:
            students =students.filter(first_name=first_name)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    def get(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)  
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
    
    def post(self,request,id):
        student=Student.objects.get(id=id)
        action=request.data.get("action")
        if action=="enroll":
            course_id=request.data.get("course_id")
            self.enroll_student(student,course_id)
            return Response(status=status.HTTP_202_ACCEPTED)
        
    def enroll_student(self,student,course_id):
        course= Course.objects.get(id=course_id)
        student.courses.add(course)

    

class ClassRoomListView(APIView):
    def get(self, request):
        classrooms = ClassRoom.objects.all()
        serializer = ClassRoomSerializer(classrooms, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name:
            students =students.filter(first_name=first_name)
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = Teacher.objects.get(id=id)  # Correct model
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)  # Changed status to HTTP_200_OK
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def post(self,request,id):
        teacher= Teacher.objects.get(id=id)
        action =request.data.get("action")
        if action=="enroll":
            course_id=request.data.get("course_id")
            self.enroll_teacher(teacher,course_id)
            return Response(status=status.HTTP_202_ACCEPTED)

    def enroll_teacher(self,teacher,course_id):
        course= Course.objects.get(id=course_id)
        teacher.courses.add(course)
    
class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        course_name=request.query_params.get("course_name")
        if course_name:
            students =students.filter(first_name=course_name)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    
    
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetailView(APIView):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def put(self, request, id):
        course = Course.objects.get(id=id)  # Correct object fetch
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)  # Changed status to HTTP_200_OK
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    def post(self,request,id):
        course=Course.objects.get(id=id)
        action=request.data.get("action")
        if action=="enroll":
            student_id=request.data.get("student_id")
            self.enroll_student(course,student_id)
            return Response(status=status.HTTP_202_ACCEPTED)
        
    def enroll_student(self,student,course_id):
        course= Course.objects.get(id=course_id)
        student.courses.add(course)
        
            
 

class ClassPeriodListView(APIView):
    def get(self, request):
        classperiods = ClassPeriod.objects.all()
        
        serializer = ClassPeriodSerializer(classperiods, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ClassPeriodDetailView(APIView):
    def get(self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classperiod)
        return Response(serializer.data)
    
    def put(self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)  # Correct object fetch
        serializer = ClassPeriodSerializer(classperiod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)  # Changed status to HTTP_200_OK
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        classperiod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  # Changed status to HTTP_204_NO_CONTENT
