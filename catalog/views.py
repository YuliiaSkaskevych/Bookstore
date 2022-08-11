from django.shortcuts import render
from .forms import ReminderForm
from .tasks import send_mail


def create_reminder(request):
    if request.method == 'POST':
        reminder_form = ReminderForm(request.POST)
        if reminder_form.is_valid():
            email = reminder_form.cleaned_data['email']
            text = reminder_form.cleaned_data['text']
            data = reminder_form.cleaned_data['datetime']
            message = "Message has sent successfully!"
            send_mail.apply_async((text, email), eta=data)
            return render(
                request,
                'catalog/create_reminder.html',
                {
                    'reminder_form': reminder_form,
                    'message': message,

                }
            )
    else:
        reminder_form = ReminderForm()
    return render(
        request,
        'catalog/create_reminder.html',
        {
            'reminder_form': reminder_form,
        }
    )
