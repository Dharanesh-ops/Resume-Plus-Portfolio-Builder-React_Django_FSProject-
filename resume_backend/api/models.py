from django.db import models


class Resume(models.Model):
    name = models.CharField(max_length=100)
    skills = models.CharField(max_length=255)
    experience = models.TextField()
    projects = models.CharField(max_length=255, default="None")
    certifications = models.CharField(max_length=255, default="None")  # Default set to "None"

    def __str__(self):
        return self.name
