from django.db import models
from django.contrib.auth.models import User

from .utils import get_data
# Create your models here.
class Item(models.Model):
	author = models.ForeignKey(User ,on_delete=models.CASCADE)
	name = models.CharField(max_length=250, blank=True)
	link = models.URLField()
	current_price = models.FloatField(blank=True)
	old_price = models.FloatField(default=0)
	price_difference = models.FloatField(default=0)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('-created',)

	def save(self, *args, **kwargs):
		name, price = get_data(self.link)
		self.current_price = price
		old_price = self.current_price

		if self.current_price:
			if price != old_price:
				diff = price - old_price
				self.price_difference = round(diff, 2)
				self.old_price = old_price
		else:
			self.old_price = 0
			self.price_difference = 0

		self.name = name

		super().save(*args, **kwargs)