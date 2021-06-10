from django.db import models

# Create your models here.

class Trial(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'user info'

    def __str__(self):
        return self.fullname