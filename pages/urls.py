from django.urls import path
from .views import homepage,aboutus

urlpatterns = [
    path('',homepage, name = 'home'),
    path('aboutus/', aboutus, name = 'aboutus')
]
