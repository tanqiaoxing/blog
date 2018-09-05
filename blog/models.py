from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):
	name = models.CharField(max_length=100)

    # def __str__(self):
    # 	return self.name

@python_2_unicode_compatible
class Tag(models.Model):
	name = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.name

@python_2_unicode_compatible
class Post(models.Model):
	title = models.CharField(max_length=50)
	body = models.TextField()
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	experpt = models.CharField(max_length=200)
	# category = models.ForeignKey(Category, on_delete=models.CASCADE)
	# tags = models.ManyToManyField(Tag)
	# author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	# def get_absolute_url(self):
	# 	return reverse('detail', kwargs={'pk': self.pk})