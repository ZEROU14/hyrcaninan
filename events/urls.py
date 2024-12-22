from django.urls import path

from .views import events , EventsDetail,SignUpCreateView,SignUpDetailView
urlpatterns = [
    path('events/',events,name='events_list'),
    path('events/<int:pk>',EventsDetail.as_view(),name='events_detail'),
    path('events/signup/detail/<int:pk>/', SignUpDetailView.as_view(), name='signup_detail'),
    path('EventSignUp/<int:pk>/',SignUpCreateView.as_view(), name = 'signupform'),
]
