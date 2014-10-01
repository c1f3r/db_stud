from rest_framework import serializers
from db.models import Group, Student


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    group_title = serializers.Field(source='group.title')
    group_id = serializers.Field(source='group.id')
    api_url = serializers.SerializerMethodField('get_api_url')
    group_api_url = serializers.SerializerMethodField('get_group_api_url')

    class Meta:
        model = Student
        fields = ('id', 'full_name', 'id_number', 'api_url', 'url', 'group_title', 'group', 'group_id', 'birth_date',
                  'group_api_url')

    @staticmethod
    def get_api_url(obj):
        return u"#/student/%s" % obj.id

    @staticmethod
    def get_group_api_url(obj):
        return u"#/group/%s" % obj.group_id


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    monitor_details = StudentSerializer(source='monitor', read_only=True)
    students_details = StudentSerializer(source='students', read_only=True)
    api_url = serializers.SerializerMethodField('get_api_url')

    class Meta:
        model = Group
        fields = ('id', 'title', 'url', 'api_url', 'monitor', 'monitor_details', 'students', 'students_details',)
        # read_only_fields = ('students',)

    @staticmethod
    def get_api_url(obj):
        return u"#/group/%s" % obj.id
