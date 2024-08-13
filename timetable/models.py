from django.db import models

# Create your models here.

from django.db import models
from course.models import Course
from teacher.models import Teacher
from student.models import Student

class Timetable(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.student} - {self.course} with {self.teacher} on {self.day_of_week}"

