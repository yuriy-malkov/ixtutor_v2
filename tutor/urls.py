from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('tutor/Booking', views.tutor_bookings, name='tutor_bookings'),
    path('user/viewAllBookings', views.view_all_bookings, name='viewAllBookings')
]
