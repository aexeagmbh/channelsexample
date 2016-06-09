import json

from channels import Group


def connect_project(message, pk):
    from main.models import Project
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        message.reply_channel.send({
            'text': json.dumps({'error': 'Project does not exist.'}),
            'close': True,
        })
        return

    group_name = Project.get_channels_group(pk)
    Group(group_name).add(message.reply_channel)


def disconnect_project(message, pk):
    from main.models import Project
    group_name = Project.get_channels_group(pk)
    Group(group_name).discard(message.reply_channel)
