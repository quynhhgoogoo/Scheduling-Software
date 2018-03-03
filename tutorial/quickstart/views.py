from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer,CourseSerializer, CourseImplementationSerializer, CourseImplementationTeacherSerializer, CurriculumSerializer, StudentGroupSerializer, TeacherSerializer
from .models import Course, CourseImplementation, CourseImplementationTeacher, Curriculum, StudentGroup, Teacher
from django.db import connection
from django.http import JsonResponse

class UserViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
	
class CourseViewSet(viewsets.ModelViewSet):
	""" 
    API endpoint that allows groups to be viewed or edited.
    """
	queryset = Course.objects.all()
	serializer_class = CourseSerializer

class CourseImplementationViewSet(viewsets.ModelViewSet):
	""" 
    API endpoint that allows groups to be viewed or edited.
    """
	queryset = CourseImplementation.objects.all()
	serializer_class = CourseImplementationSerializer

class CurriculumViewSet(viewsets.ModelViewSet):
	""" 
    API endpoint that allows groups to be viewed or edited.
    """ 
	queryset = Curriculum.objects.all()
	serializer_class = CurriculumSerializer

class StudentGroupViewSet(viewsets.ModelViewSet):
	""" 
    API endpoint that allows groups to be viewed or edited.
    """ 
	queryset = StudentGroup.objects.all()
	serializer_class = StudentGroupSerializer

class TeacherViewSet(viewsets.ModelViewSet):
	""" 
    API endpoint that allows groups to be viewed or edited.
    """ 
	queryset = Teacher.objects.all()
	serializer_class = TeacherSerializer

class CourseImplementationTeacherViewSet(viewsets.ModelViewSet):
	""" 
    API endpoint that allows groups to be viewed or edited.
    """ 
	queryset = CourseImplementationTeacher.objects.all()
	serializer_class = CourseImplementationTeacherSerializer
	
def teacher_course(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT distinct teacher.name, course.name FROM course, `course_implementation`, `course_implementation_teacher`, teacher WHERE `course_implementation_teacher`.teacherid = teacher.id AND course.id = `course_implementation_teacher`.`course implementationid`")
        rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append({"teacher":row[0],"course":row[1]})
    return JsonResponse(data, safe=False)

def student_course(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT name, course.group FROM `course`")
        rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append({"course":row[0],"group":row[1]})
    return JsonResponse(data, safe=False)

def teacher_degree(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT teacher.name, student_group.degree_program from teacher, student_group, course_implementation, course_implementation_teacher where course_implementation.courseid = `course_implementation_teacher`.`course implementationid`")
        rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append({"teacherName":row[0],"degree":row[1]})
	return JsonResponse(data, safe=False)