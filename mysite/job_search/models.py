from django.db import models

def JobInfo(self):
    job_name = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    