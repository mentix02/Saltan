from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
	user = models.OneToOneField(User, unique=True)
	profile_pic = models.ImageField(upload_to='user_images/', blank=False)

	def __str__(self):
		return self.user.username


class Salt(models.Model):
	creator = models.ForeignKey(Profile)
	title = models.CharField(max_length=50, blank=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	description = models.TextField(max_length=450, blank=False)
	image = models.ImageField(upload_to='salt_images/', blank=False)

	def __str__(self):
		return self.title


class Comment(models.Model):
	user = models.ForeignKey(Profile)
	salt = models.ForeignKey(Salt)
	comment = models.TextField(max_length=300)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return self.comment


class CommentReply(models.Model):
	user = models.ForeignKey(Profile)
	comment = models.ForeignKey(Comment)
	reply = models.TextField(max_length=300)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return self.reply


class Pepper(models.Model):
	user = models.ForeignKey(Profile)
	body = models.TextField(max_length=110)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return str(self.user.user.username) + self.body
