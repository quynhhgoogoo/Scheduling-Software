# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Course, CourseImplementation, CourseImplementationTeacher, Curriculum, Group, Teacher

admin.site.register(Course)
admin.site.register(CourseImplementation)
admin.site.register(CourseImplementationTeacher)
admin.site.register(Curriculum)
admin.site.register(Group)
admin.site.register(Teacher)
