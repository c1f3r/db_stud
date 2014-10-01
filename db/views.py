from rest_framework import generics
from rest_framework import permissions
from db.models import Group, Student
from db.serializers import GroupSerializer, StudentSerializer
from django.views import generic


class ForTagTest(generic.ListView):
    model = Group


class GroupList(generics.ListCreateAPIView):
    """
    List all group or add new group
    """
    model = Group
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
                         
                         
class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    """                  
    Retrieve, update or delete a Group
    """                  
    model = Group        
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class StudentList(generics.ListCreateAPIView):
    """
    List all students
    """
    model = Student
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a student.
    """
    model = Student
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
