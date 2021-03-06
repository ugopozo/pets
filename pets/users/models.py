from django.db import models
from django.contrib.auth.models import AbstractUser
from users.validators import validate_facebook_url
from django.core.urlresolvers import reverse


class OwnerProfile(AbstractUser):
    is_information_confirmed = models.BooleanField(default=False)
    facebook = models.CharField(max_length=250, blank=True, null=True,
                                validators=[validate_facebook_url])

    def get_absolute_url(self):
        return reverse('users:user_profile', args=[self.id])

    def __str__(self):
        return self.username
