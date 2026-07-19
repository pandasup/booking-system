from django.contrib import admin

from booking.models import BookingModel, EventModel, TicketModel

# Register your models here.
admin.site.register(EventModel)
admin.site.register(TicketModel)
admin.site.register(BookingModel)