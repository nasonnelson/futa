from django.db import models
from django.forms import ModelForm

# Create your models here.

class Agents(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    photo = models.ImageField()

    def __str__(self):
        return self.first_name

class About(models.Model):
    jina_kitu = models.CharField(max_length=200)
    maelezo = models.TextField(max_length=1000000)
    picha = models.ImageField()

    def __str__(self):
        return self.jina_kitu

class Comment(models.Model):
    jina = models.CharField(max_length=200)
    phone = models.IntegerField()
    maoni = models.TextField(max_length=100000)

    def __str__(self):
        return self.jina

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['jina', 'phone', 'maoni']

class Photo(models.Model):
    picha = models.ImageField()
    maelezo = models.TextField(max_length=1000000)

class Video(models.Model):
    video = models.FileField()
    maelezo = models.TextField(max_length=1000000)

class Slide(models.Model):
    picha = models.ImageField()