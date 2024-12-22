from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
from django.urls import reverse_lazy,reverse
from .models import Events,Event_SignUp
from .forms import SignUpForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
# Create your views here.
def events(request):
    events = Events.objects.all().order_by('-date_time_created')
    return render(request,'events/events_list.html',{
        "event": events

    })

class EventsDetail(generic.DetailView):
    model = Events
    template_name = 'events/events_detail.html'
    context_object_name = 'events'



# views.py


class SignUpCreateView(generic.CreateView):
    model = Event_SignUp
    form_class = SignUpForm
    template_name = 'events/events_signup.html'
    # success_url = reverse_lazy('signup_detail')  # Redirect to a success page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = get_object_or_404(Events, id=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        signup = form.save(commit=False)
        event = get_object_or_404(Events, id=self.kwargs['pk'])
        signup.event = event
        signup.save()  # Ensure the object is saved
        

        messages.success(self.request,_('your sign up was succsuful'))
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('signup_detail', kwargs={'pk': self.object.pk})



class SignUpDetailView(generic.DetailView):
    model = Event_SignUp
    template_name = 'events/signup_detail.html'
    context_object_name = 'signup'

 
    def form_valid(self, form):
        signup = form.save(commit=False)
        event = get_object_or_404(Events, id=self.kwargs['pk'])
        signup.event = event
        signup.save()  # Ensure the object is saved
        