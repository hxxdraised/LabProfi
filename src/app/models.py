from django.db import models
from django.contrib.auth.models import User

class Specialist(models.Model):
    name = models.CharField(max_length=40, unique=True)
    desc = models.TextField(null=True, blank=True)
    preview_image = models.ImageField(upload_to="specialist_preview_img", blank=True, null=True)

    def __str__(self):
        return f'''Специалист "{self.name}"'''
