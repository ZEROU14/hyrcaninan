from .models import Events,Event_SignUp
from django.db.models import Sum
def events(request):
    # events = Events.objects.all()
    return {
        "event": Events.objects.filter(status=True).order_by('-date_time_created'),
        
    }

def events4(request):
    # events = Events.objects.all()
    return {
        "events": Events.objects.count(),  
    } 

def Event_signup(request):
    return {
        'event_signup': Event_SignUp.objects.count()
    }

def events_km(request):
    return {
       'kilometers': Events .objects.aggregate(Sum('kilometers'))['kilometers__sum'] or 0
    }

def events2(request):
    return {
        'new_event': Events.objects.filter(status=True).order_by('-date_time_created').first(),
    }