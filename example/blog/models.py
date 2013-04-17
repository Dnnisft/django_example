from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse

class Post(models.Model):
	title = models.CharField(max_length=100,unique=True)
	slug = models.SlugField(max_length=100,unique=True)
	content = models.TextField(blank=True)
	tags = TaggableManager(blank=True)
	meta_desc = models.CharField(max_length=150,blank=True)
	author = models.ForeignKey(User)

	def __unicode__(self):
		return "%s" % self.title

	def get_absolute_url(self):
		return reverse('showpost',args=[str(self.category.slug),str(self.slug)])