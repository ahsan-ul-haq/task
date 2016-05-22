"""
Model for saving UserInfo.
"""
from django.db import models


class UserInfo(models.Model):
    """ Model to save User Information. """
    name = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
