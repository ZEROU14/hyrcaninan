from .models import AboutUs,Sponsers





def aboutus(request):
    try:
        aboutus_object = AboutUs.objects.get(pk=1)
    except AboutUs.DoesNotExist:
        aboutus_object = None
    return {
        'aboutus': aboutus_object
    }

def sponsers(request):
    return {
        'sponser': Sponsers.objects.all()
    }


# context_processors.py
