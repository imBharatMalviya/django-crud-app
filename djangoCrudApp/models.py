from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


class Posts(models.Model):
    title = models.CharField(max_length=35)
    content = models.CharField(max_length=400)
    created_on = models.DateTimeField(default=timezone.now)