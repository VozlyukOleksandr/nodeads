from django.db import models
from django.utils.timezone import now
# Create your models here.


class Group(models.Model):
    name=models.CharField(max_length=64, null=False)
    description=models.CharField(max_length=512,null=False)
    icon=models.ImageField(default='/icons/icon.png')
    group_id=models.IntegerField()


    def __str__(self):
        return self.name

class Element(models.Model):

    name=models.CharField(max_length=64, null=False)
    description=models.CharField(max_length=512, null=True)
    icon = models.ImageField(default='/icons/icon.png')
    create_time=models.DateField(null=False, default=now())
    moderator=models.BooleanField(default=False)
    group_id=models.IntegerField()

    def __str__(self):
        return self.name