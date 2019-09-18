from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    #path('tutor/booking', views.tutor_create_bookings, name='tutorBookings'),
    path('user/viewAllBookings', views.view_all_bookings, name='viewAllBookings'),
    path(r'user/bookings/<int:bookingID>', views.booking_information, name='bookingInformation')
]