# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from db.models import Group


class Command(BaseCommand):
    def handle(self, *args, **options):
        groups = Group.objects.all()
        for group in groups:
            index = 0
            students = group.students.all()

            print u'Group "%s":' % group.title

            for student in students:
                index += 1
                print u'%s %s' %(index, student.full_name)