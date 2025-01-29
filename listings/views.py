from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Booking
from .serializers import BookingSerializer
from .tasks import send_booking_confirmation_email
#from django.db import ...

class BookingViewSet(ModelViewSet):
        queryset = Booking.objects.all()
            serializer_class = BookingSerializer

                def perform_create(self, serializer):
                            # Save the booking instance
                                    booking = serializer.save()

                                            # Trigger the email task asynchronously
                                                    subject = "Booking Confirmation"
                                                            message = f"Dear {booking.customer_name}, your booking (ID: {booking.id}) has been confirmed."
                                                                    recipient_list = [booking.customer_email]

                                                                            send_booking_confirmation_email.delay(subject, message, recipient_list)



# Create your views here.
