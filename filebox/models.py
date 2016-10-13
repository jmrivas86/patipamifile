import json
from django.db import models
from django.contrib.auth.models import User
from channels import Group


class Box(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(User)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def totalfiles(self):
        """
        Returns the Channels Group name to use for sending notifications.
        """
        return self.filebox_set.count()

    class Meta:
        ordering = ["create_date"]


class Filebox(models.Model):
    name = models.CharField(max_length=200)
    file_box = models.FileField(upload_to='uploads/')
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    upload_by = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def send_notification(self):
        """
        Sends a notification to everyone in our Liveblog's group with our
        content.
        """
        notification = {
            "id": self.id,
            "file_name": self.name,
            "file_box_url": self.file_box.url,
            "total_files": self.box.totalfiles,
            "box_id": self.box.id
        }
        Group("box").send({
            # WebSocket text frame, with JSON content
            "text": json.dumps(notification),
        })

    def save(self, *args, **kwargs):
        """
        Hooking send_notification into the save of the object
        """
        result = super(Filebox, self).save(*args, **kwargs)
        self.send_notification()
        return result

    class Meta:
        ordering = ["create_date"]
