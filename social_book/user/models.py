from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

class CustomUser(AbstractUser):
    public_visibility = models.BooleanField(default=True)
    birth_year = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.birth_year:
            self.age = datetime.date.today().year - self.birth_year
        super().save(*args, **kwargs)

class UploadedFile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='uploaded_books/')
    visibility = models.BooleanField(default=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    year_published = models.IntegerField()

    def __str__(self):
        return self.title
