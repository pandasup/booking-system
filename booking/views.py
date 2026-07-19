from django.shortcuts import redirect, render

from booking.models import EventModel

# Create your views here.
def events_list_view(request):
    events = EventModel.objects.all()
    context = {
        'events': events
    }
    return render(request, 'events/list.html', context)

def event_detail_view(request, pk):
    pass

def event_create_view(request):
    pass

def event_update_view(request, pk):
    pass

def event_delete_view(request, pk):
    event = get_object_or_404(EventModel, pk=pk)

    event.delete()
    return redirect('events-list')


#Tickets

def tickets_list_view(request):
    pass

def ticket_create_view(request):
    pass    

def ticket_update_view(request, pk):
    pass

def ticket_delete_view(request, pk):
    pass