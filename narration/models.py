from django.db import models
from django.utils import timezone
class Content(models.Model):
	"""docstring for Content"""
	title = models.CharField(max_length = 200)
	text = models.TextField()
	
	def __str__(self):
		return self.title

class Images(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField()
    #created_date = models.DateTimeField(
    #       default=timezone.now)
	def __str__(self):
		return self.name

#class Images(models.Model):
	#content = models.ForeignKey(Content, related_name= 'images' , on_delete = 'CASCADE')
#	image = models.ImageField(upload_to = 'photos')