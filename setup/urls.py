from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from school.views import (CoursesViewSet, EnrollmentViewSet,
                          ListEnrollmentsStudent, ListStudentsEnrolled,
                          StudentsViewSet)

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Students')
router.register('cursos', CoursesViewSet, basename='Courses')#in pt-br to work along with the REACT API
router.register('enrollments', EnrollmentViewSet, basename='Enrollments')

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('general-control/', admin.site.urls),
    path('', include(router.urls) ),
    path('students/<int:pk>/enrollments/', ListEnrollmentsStudent.as_view()),
    path('cursos/<int:pk>/enrollments/', ListStudentsEnrolled.as_view())
]
