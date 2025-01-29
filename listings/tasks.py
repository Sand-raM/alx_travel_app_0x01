
#from django.db import ...
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(subject, message, recipient_list):
        send_mail(
                        subject,
                                message,
                                        'gabrieltuyishimire35@gmail.com',  # Replace with your "from" email address
                                                recipient_list,
                                                        fail_silently=False,
                                                            )
        return f"Email sent to {', '.join(recipient_list)}"

