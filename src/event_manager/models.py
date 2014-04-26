from django.db import models
from django.contrib.auth.models import User, Group

class Location(models.Model):
	x = models.DecimalField(
		max_digits=10,
		decimal_places=5
	)
	y = models.DecimalField(
		max_digits=10,
		decimal_places=5
	)

class Suggestion(models.Model):
	YES = 'Y'
	NO = 'N'
	MAYBE = 'M'
	NONE = 'O'
	RESPONSE_CHOICES = (
		(YES, 'Yes'),
		(NO, 'No'),
		(MAYBE, 'Maybe'),
		(NONE, 'No vote'),
	)
	
	user = models.ForeignKey(User)
	response = models.CharField(
		max_length=1,
		choices=RESPONSE_CHOICES,
		default=NONE)
	time = models.DateTimeField(
		null=True,
		blank=True
	)
	location = models.ForeignKey(
		Location,
		null=True,
		blank=True
	)
	group = models.ForeignKey(
		Group,
		null=True,
		blank=True
	)
	#activity=


class Event(models.Model):
	owner = models.ForeignKey(
		User,
		related_name='owner'
	)
	invites = models.ManyToManyField(User, through='Invite')
	description = models.TextField()
	location = models.ForeignKey(Location)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField(
		null=True,
		blank=True
	)

	def get_dict(self):
		return 	{
			"event_id": self.id,
			"event_owner": self.owner_id,
			"event_description": self.description,
			"event_location_id": self.location_id,
			"event_start_time": self.start_time,
			"event_end_time": self.end_time,
		}

class Invite(models.Model):
	YES = 'Y'
	NO = 'N'
	MAYBE_YES = 'MY'
	MAYBE_NO = 'MN'
	NONE = 'O'
	RSVP_CHOICES = (
		(YES, 'Yes'),
		(NO, 'No'),
		(MAYBE_YES, 'Maybe Yes'),
		(MAYBE_NO, 'Maybe No'),
		(NONE, 'No response'),
	)
	event = models.ForeignKey(Event)
	user = models.ForeignKey(User)
	rsvp = models.CharField(
		max_length=2,
		choices=RSVP_CHOICES,
		default=NONE
	)

