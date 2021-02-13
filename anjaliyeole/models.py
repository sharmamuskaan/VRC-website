from django.db import models
from django.conf import settings

# Create your models here.
achievements= (
    ('Certifications','Certifications'),
    ('Publications','Publications'),
    ('Copyrights','Copyrights'),
    ('Patents','Patents'),
    ('Projects','Projects'),
    ('Webinars','Webinars'),
	('Articles','Articles'))


class About(models.Model):
	description = models.TextField()
	image = models.ImageField(upload_to='static')

	class Meta:
		verbose_name ="About"
		verbose_name_plural = "About"

	def __str__(self):
		return 'description'


class Book(models.Model):
	name = models.CharField(max_length =200)
	published = models.DateField(auto_now=False)
	picture = models.ImageField(upload_to='static/books',max_length=255,null=True)
	buy_link = models.URLField(max_length = 200, default ="default")

	def __str__(self):
		return self.name


class Award(models.Model):
	award = models.CharField(max_length =200)
	image = models.ImageField(upload_to='static/awards',)
	year = models.IntegerField()
	description = models.TextField()

	def __str__(self):
		return self.award

'''
class AreasOfExpertise(models.Model):
	title = models.CharField(max_length =200)

	def __str__(self):
		return self.name

class Education(models.Model):
	degree = models.CharField(max_length =200)
	institute = models.CharField(max_length =200)
	year = models.IntegerField()

	def __str__(self):
		return self.name

'''

class Interaction(models.Model):
    category = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.category

class ContactMe(models.Model):
	name = models.CharField(max_length =200)
	subject = models.CharField(max_length =200)
	message = models.TextField()
	email = models.EmailField(max_length=200)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name ="ContactMe"
		verbose_name_plural = "ContactMe"



class Achievement(models.Model):
	category = models.CharField(choices=achievements, max_length=200)
	content = models.TextField()

	def __str__(self):
		tag = self.category
		return tag