from django.db import models

from model_utils.models import TimeStampedModel

from main.mixins import PushNotificationOnChangeModelMixin


class Project(PushNotificationOnChangeModelMixin, TimeStampedModel):
    name = models.TextField()

    def __str__(self):
        return self.name

    @staticmethod
    def get_channels_group(pk):
        return 'project-{pk}'.format(pk=pk)


class Asset(PushNotificationOnChangeModelMixin, TimeStampedModel):
    name = models.TextField()
    project = models.ForeignKey(Project)

    def __str__(self):
        return '{} ({})'.format(self.name, self.project)

    @staticmethod
    def get_channels_group(pk):
        return 'project-{pk}'.format(pk=pk)
