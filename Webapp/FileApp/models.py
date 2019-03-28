from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class files(models.Model):
    FileName=models.CharField(max_length=100)
    file=models.FileField(null=True,blank=True,upload_to='Files')
    content=models.TextField()
    date_upload=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.FileName


    def get_absolute_url(self):
        return reverse("file-detail", kwargs={"pk": self.pk})
    