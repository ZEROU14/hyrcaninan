from django.urls import path

from .views import BlogsList,BLogDetail

urlpatterns = [
    path('blogs_list/',BlogsList.as_view() ,name='blogs' ),
    path('blogs_detail/<int:pk>/',BLogDetail.as_view(),name='blog_detail')
]
