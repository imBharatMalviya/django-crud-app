from django.forms import ModelForm, TextInput, Textarea
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from .models import Posts
import logging

logger = logging.getLogger(__name__)


class PostForm(ModelForm):
    class Meta:
        model = Posts
        exclude = ['created_on']
        widgets = {
            "title": TextInput(attrs={'class': 'form-control'}),
            "content": Textarea(attrs={'class': 'form-control'})
        }
