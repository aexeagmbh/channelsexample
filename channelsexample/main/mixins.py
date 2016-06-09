import json

from channels import Group


class Action:
    CREATED = 'created'
    UPDATED = 'updated'
    DELETED = 'deleted'


class PushNotificationOnChangeModelMixin:

    @staticmethod
    def get_channels_group(obj):
        return 'db-object-{pk}'.format(pk=obj.pk)

    def save(self, *args, **kwargs):
        action = Action.CREATED if self.id is None else Action.UPDATED

        result = super().save(*args, **kwargs)
        self._notify_websockets_about_model_change(action=action)
        return result

    def delete(self, *args, **kwargs):
        self._notify_websockets_about_model_change(action=Action.DELETED)
        return super().delete(*args, **kwargs)

    def _notify_websockets_about_model_change(self, action):
        data = {
            'pk': self.pk,
            'action': action,
        }

        group_name = self.get_channels_group(pk=self.project.pk)
        Group(group_name).send({
            'text': json.dumps(data),
        })
