from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer,CourseSerializer, CourseImplementationSerializer, CourseImplementationTeacherSerializer, CurriculumSerializer, GroupSerializer, TeacherSerializer
from .models import Course, CourseImplementation, CourseImplementationTeacher, Curriculum, Group, Teacher

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

class GroupViewSet(viewsets.ModelViewSet):
	""" 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

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