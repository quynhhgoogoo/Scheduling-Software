from django.contrib.auth.models import User, Group
from .models import Course, CourseImplementation, CourseImplementationTeacher, Curriculum, Studentgroup, Teacher
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('url', 'id', 'curriculumid', 'code', 'language', 'name', 'credit', 'group')
        
class CourseImplementationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseImplementation
        fields = ('url', 'id', 'group', 'courseid')

class CurriculumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curriculum
        fields = ('url', 'id', 'group_code')
        
class StudentgroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Studentgroup
        fields = ('url', 'id', 'code', 'degree_program', 'curriculumid')
        
class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ('url', 'id', 'code', 'name')
        
class CourseImplementationTeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'course_implementationid', 'teacherid', 'p1', 'p2', 'p3', 'p4', 'p5')