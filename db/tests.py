from django.contrib.auth.models import User
from db.models import Group, Student
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class GroupTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username="Tester", email="tester@example.loc",
                                                  password='parol')

    def test_create_group_anon(self):
        """
        Ensure we can't create a new group object while not authorized.
        """
        url = reverse('group-list')
        data = {'title': 'TestGroup'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_group_login(self):
        """
        Ensure we can create a new group object.
        """
        url = reverse('group-list')
        data = {'title': u'TestGroup'}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_student(self):
        url = reverse('student-list')
        data = {'full_name': u"TestStudent", 'id_number': "007", 'birth_date': '2000-01-01'}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)