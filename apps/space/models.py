from django.db import models


class Space(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='static/spaces')


class Folder(models.Model):
    name = models.CharField(max_length=255)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)


class List(models.Model):
    name = models.CharField(max_length=255)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, blank=True, null=True)
