from django.db import models

# Create your models here.
class Ad(models.Model):
	image = models.ImageField(default = 'default.jpg', upload_to = 'advert_images')
	def __str__(self):
		return f"Ad_id - {self.id} "#Determines how these images are named when queried or in the backend

class Interaction(models.Model):
	ad_1 = models.PositiveSmallIntegerField(default = 0)
	ad_2 = models.PositiveSmallIntegerField(default = 0)
	ad_3 = models.PositiveSmallIntegerField(default = 0)
	ad_4 = models.PositiveSmallIntegerField(default = 0)
	ad_5 = models.PositiveSmallIntegerField(default = 0)
	ad_6 = models.PositiveSmallIntegerField(default = 0)
	ad_7 = models.PositiveSmallIntegerField(default = 0)
	ad_8 = models.PositiveSmallIntegerField(default = 0)
	ad_9 = models.PositiveSmallIntegerField(default = 0)
	ad_10 = models.PositiveSmallIntegerField(default = 0)