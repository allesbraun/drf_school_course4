from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from school.models import Course, Enrollment, Student
from school.serializer import (CourseSerializer, EnrollmentSerializer,
                               ListEnrollmentsStudentSerializer,
                               ListStudentsEnrolledSerializer,
                               StudentSerializer, StudentSerializerV2)


class StudentsViewSet(viewsets.ModelViewSet):
    """Exhibiting all students"""
    queryset = Student.objects.all()
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        else:
            return StudentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    """Exhibiting all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ['get', 'post', 'put', 'path', 'delete']
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        # header Location
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status= status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response

class EnrollmentViewSet(viewsets.ModelViewSet):
    """Exhibiting all enrollments"""
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    http_method_names = ['get', 'post', 'put', 'path']

class ListEnrollmentsStudent(generics.ListAPIView):
    """Listing all enrollments of a student"""
    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListEnrollmentsStudentSerializer

class ListStudentsEnrolled(generics.ListAPIView):
    """Listing all students enrolled in a course"""
    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListStudentsEnrolledSerializer

