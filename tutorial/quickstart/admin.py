# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Course, CourseImplementation, CourseImplementationTeacher, Curriculum, Studentgroup, Teacher

admin.site.register(Course)
admin.site.register(CourseImplementation)
admin.site.register(CourseImplementationTeacher)
admin.site.register(Curriculum)
admin.site.register(Studentgroup)
admin.site.register(Teacher)
