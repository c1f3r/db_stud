from django.db import models

# Create your models here.
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Group(models.Model):
    title = models.CharField(u"Group title", max_length=20, blank=False, unique=True)
    monitor = models.ForeignKey('Student', related_name="monitor", blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title


class Student(models.Model):
    group = models.ForeignKey(Group, related_name="students", blank=True, null=True, on_delete=models.SET_NULL)
    full_name = models.CharField(u"Student's full name", max_length=50, blank=False)
    id_number = models.CharField(u"Number of student's ID", max_length=20, blank=True, unique=True)
    birth_date = models.DateField(u"Student's date of birth", blank=True)

    class Meta:
        ordering = ['full_name']

    def __unicode__(self):
        return self.full_name


class Event(models.Model):
    time = models.DateTimeField('Date/Time', auto_now=True)
    action = models.CharField('Action', max_length=20)
    model = models.CharField('Model', max_length=50)

    class Meta:
        ordering = ['-time']

    def __unicode__(self):
        return self.model

@receiver(post_save, sender=Group)
@receiver(post_save, sender=Student)
def create_modify_signal(sender, instance, *args, **kwargs):
    event = Event()
    event.model = instance
    try:
        sender.objects.get(pk=instance.pk)
        event.action = u'modified'
    except sender.DoesNotExist:
        event.action = u'created'
    event.save()

@receiver(post_delete, sender=Group)
@receiver(post_delete, sender=Student)
def delete_signal(sender, instance, *args, **kwargs):
    event = Event()
    event.model = instance
    event.action = u'deleted'
    event.save()