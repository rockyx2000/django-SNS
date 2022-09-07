from django.db import models
import uuid

# Create your models here.

def image_directory_path(instance, filename):
    return 'uploads/{}.{}'.format(str(uuid.uuid4()), filename.split('.')[-1])

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    sns_image = models.ImageField(upload_to= image_directory_path)
    good = models.IntegerField()
    read = models.IntegerField()
    read_text = models.TextField()