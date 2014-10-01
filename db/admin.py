from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django import forms
from db.models import Group, Student, Event
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ('full_name', 'id_number', 'birth_date', 'group',)
    search_fields = ['full_name',]


class StudentInline(admin.TabularInline):
    model = Student


class GroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.fields['monitor'].queryset = self.instance.students.all()


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    model = Group
    form = GroupForm
    list_display = ('title', 'get_students_quantity', 'get_monitor',)
    inlines = [StudentInline, ]

    def get_students_quantity(self, obj):
        return obj.students.all().count()

    get_students_quantity.short_description = "Students quantity"

    def get_monitor(self, obj):
        return obj.monitor

    get_monitor.short_description = "Monitor"


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ['model', 'action', 'time']
    search_fields = ['model']