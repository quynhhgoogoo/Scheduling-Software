from django.conf.urls import url, include
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'teacher', views.TeacherViewSet)
router.register(r'curriculums', views.CurriculumViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'studentgroups', views.StudentGroupViewSet)
router.register(r'courseimplementation', views.CourseImplementationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^teachercourse/$', views.teacher_course, name='teacher_course'),
    url(r'^studentcourse/$', views.student_course, name='student_course'),
	url(r'^teacherdegree/$', views.teacher_degree, name='teacher_degree'),
]
