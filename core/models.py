from django.db import models

from django.contrib.auth.models import User
from django.db import models
from cars.models import Car
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Car, on_delete=models.CASCADE)  # Replace with your item model

    class Meta:
        unique_together = ('user', 'item')  # Ensure a user can't favorite the same item twice
class FavouriteManager(models.Manager):
    def get_favorites_for_user(self, user):
        """Returns all items that are favorited by the given user."""
        return self.filter(user=user).select_related('item')