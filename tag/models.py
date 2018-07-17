from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Player(models.Model):
	password=models.TextField()
	x=models.IntegerField(
		validators=[MinValueValidator(0), MaxValueValidator(63)],
	)
	y=models.IntegerField(
		validators=[MinValueValidator(0), MaxValueValidator(63)],
	)
