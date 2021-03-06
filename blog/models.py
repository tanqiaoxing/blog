from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		# return self.name
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    experpt = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # img = models.ForeignKey('Img', on_delete=models.CASCADE, blank=True, null=True)
    img = models.ImageField(upload_to='./img/', blank=True, null=True)

    def __str__(self):
        return self.title
