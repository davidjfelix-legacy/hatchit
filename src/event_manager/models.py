from django.db import models


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
	time = models.DateTime(
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

class Location(models.Model):
	x = models.DecimalField(
		max_digits=10,
		decimal_digits=5
	)
	y = models.DecimalField(
		max_digits=10,
		decimal_digits=5
	)

	
class Event(models.Model):
	owner = models.ForeignKey(User)
	invites = models.ManyToManyField(User, through='Invite')
	description = models.TextField()
	location = models.ForeignKey(Location)
	start_time = models.DateTime()
	end_time = models.DateTime(
		null=True,
		blank=True
	)


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

