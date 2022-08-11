from django import forms
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError


class ReminderForm(forms.Form):
    email = forms.EmailField(max_length=100, required=True)
    text = forms.CharField(max_length=300, required=True)
    datetime = forms.DateTimeField(help_text="Example: YYYY-MM-DD hh:mm:ss")

    def clean_datetime(self):
        data = self.cleaned_data['datetime']
        today_now = timezone.now()
        if today_now < data < today_now + datetime.timedelta(days=2):
            raise ValidationError('Invalid date')
        return data
