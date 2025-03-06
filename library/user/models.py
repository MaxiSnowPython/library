from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="documents/", null=True, blank=True)
    data = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('user', 'title')

    def __str__(self):
        return self.title
