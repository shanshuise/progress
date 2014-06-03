from django.db import models

class Progress(models.Model):
    PROGRESS_CHOICES = (
        (u'1', u')
    )
    username = models.ForeignKey(User)
    pname = models.CharField(max_length=50)
    pprogress = models.CharField(max_length=50, choices=PROGRESS_CHOICES)
