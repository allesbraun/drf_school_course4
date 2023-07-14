from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from school.models import Course


class CoursesTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Courses-list')
        self.course_1 = Course.objects.create(
            code_course = 'CT1', description = 'Course test one', level = 'B'
        )
        self.course_2 = Course.objects.create(
            code_course = 'CT2', description = 'Course test two', level = 'I'
        )
    
    # def test_failer(self):
    #     self.fail('Test intentionally failed, do not worry!')
    def test_verb_GET_to_list_courses(self):
        """Test to verify if the verb GET is listing the courses"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    
    def test_verb_POST_to_create_courses(self):
        """Test to verify if the verb POST is creating the courses"""
        data = {
            'code_course' : 'CT3',
            'description' : 'Course test three',
            'level' : 'A'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        
    def test_verb_DELETE_to_delete_courses(self):
        """Test to verify if the verb DELETE is deleting the courses"""
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_verb_PUT_to_update_course(self):
        """Test to verify if the verb PUT is updating the courses"""
        data = {
            'code_course' : 'CT31',
            'description' : 'Course test one updated',
            'level' : 'A'
        }
        response = self.client.put('/cursos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)