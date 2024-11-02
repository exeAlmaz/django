import pytest
from rest_framework.test import APIClient

from students.models import Student, Course
from model_bakery import baker
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from django.urls import reverse


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student():
    def factory_student(*args, **kwargs):
        return baker.make("Student", **kwargs)

    return factory_student


@pytest.fixture
def course():
    def factory_course(*args, **kwargs):
        return baker.make("Course", **kwargs)

    return factory_course


# @pytest.mark.django_db
# def test_retrieve(client, course):
#     the_course = course(_quantity=1)
#     id_course = the_course[0].id
#     name_course = the_course[0].name
#
#     response = client.get('/courses/'f'{id_course}/')
#     data = response.json()
#     assert response.status_code == HTTP_200_OK
#
#     assert data.get('id') == id_course
#     assert data.get('name') == name_course
#
# @pytest.mark.django_db
# def test_list(client, course):
#     the_course = course(_quantity=5)
#     response = client.get('/courses/')
#     assert response.status_code == HTTP_200_OK
#     data = response.json()
#     assert len(data) == 5
#
#
#
# @pytest.mark.django_db
# def test_retrieve(client, course):
#     course_list = course(_quantity=1)
#     course_id = course_list[0].id
#     course_name = course_list[0].name
#     response = client.get('/courses/')
#     assert response.status_code == HTTP_200_OK
#     print(course_name)
#
# @pytest.mark.django_db
# def test_filter(client, course):
#     course_list = course(_quantity=6)
#     course_id = course_list[3].id
#     response = client.get('/courses/', {'id': course_id})
#     data = response.json()
#     assert response.status_code == HTTP_200_OK
#     assert data[0]["id"] == course_list[3].id
#
@pytest.mark.django_db
# def test_name(client, course):
#     course_list = course(_quantity=10)
#     course_name = course_list[5].name
#     response = client.get('/courses/', {'name': course_name})
#     data = response.json()
#     assert data[0]['name'] == course_list[5].name

@pytest.mark.django_db
def test_create(client):
    course_name = 'course'
    data = {'name': 'course'}
    response = client.post('/courses/', data)
    assert response.status_code == HTTP_201_CREATED
    data_new = response.json()
    assert course_name == data_new["name"]

@pytest.mark.django_db
def test_update(client, course):
    course_data = course(name='Course_old')
    url = reverse('courses-detail', args=(course_data.id, ))
    upd_course = "Course_new"
    data = {'name': upd_course}
    response = client.patch(url, data)
    assert response.status_code == HTTP_200_OK
    data_new = response.json()
    assert data_new['name'] == upd_course

@pytest.mark.django_db
def test_delete(client, course):
    course_data = course(name='Course_3')
    url = reverse('courses-detail', args=(course_data.id, ))
    response = client.delete(url)
    assert response.status_code == HTTP_204_NO_CONTENT
    assert len(Course.objects.filter(name="Course_3")) == 0



