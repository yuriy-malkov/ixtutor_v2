from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.register, name='user_register'),
    path('user_login', views.login, name='user_login'),
    # path('tutor/booking', views.tutorBookings, name='tutorBooking'),
    path('user/viewAllBookings', views.view_all_bookings, name='viewAllBookings'),
    path('user/bookings/<int:bookingID>', views.booking_information, name='bookingInformation'),
    path('user/userType', views.userType, name='userType')
]