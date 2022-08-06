from django import forms


class ReminderForm(forms.Form):
    email = forms.EmailField(max_length=100, required=True)
    text = forms.CharField(max_length=300, required=True)
    datetime = forms.DateTimeField(help_text="Example: YYYY-MM-DD hh:mm:ss")
