from django.db import models
from django.utils import timezone

class Event(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	hashtag = models.CharField(max_length=15, blank=True, null=True)
	startDate = models.DateTimeField(default=timezone.now)
	endDate = models.DateTimeField(default=timezone.now)
	instructions = models.TextField(blank=True, null=True)
	prizes = models.TextField(blank=True, null=True)
	link = models.CharField(max_length=200, blank=True, null=True)
	imagePath = models.CharField(max_length=200, blank=True, null=True)

	PRIVATE = 'PRI'
	PUBLIC = 'PUB'
	EVENT_VISIBILITY_CHOICES = (
		(PRIVATE, "Private"),
		(PUBLIC, "Public"),
	)
	visibility = models.CharField(max_length=3, choices=EVENT_VISIBILITY_CHOICES, default=PUBLIC)
	noSocialSharing = models.BooleanField(default=False)
	password = models.CharField(max_length=10, blank=True, null=True)

	def __str__(self):
		return self.title

class Question(models.Model):
	event = models.ForeignKey(Event, related_name='questions')
	qTitle = models.CharField(max_length=200)
	qExplanation = models.TextField()

	VIDEO = 'V'
	PHOTO = 'P'
	QUESTION_TYPE_CHOICES = (
		(VIDEO, 'Video'),
		(PHOTO, 'Photo'),
	)
	qType = models.CharField(max_length=2,
									  choices=QUESTION_TYPE_CHOICES,
									  default=PHOTO)

	qPoints = models.IntegerField()

	def __str__(self):
		return self.qTitle

class Participant(models.Model):
	event = models.ForeignKey(Event, related_name='participants')
	twitterHandle = models.CharField(max_length=20)

	def __str__(self):
		return self.twitterHandle

class Answer(models.Model):
	question = models.ForeignKey(Question, related_name='answers')
	participant = models.ForeignKey(Participant, related_name='answers')
	tweetId = models.CharField(max_length=20)
	tweetText = models.CharField(max_length=140)
	scoring = models.IntegerField()
	judgeComments = models.TextField()

	def __str__(self):
		return self.tweetText