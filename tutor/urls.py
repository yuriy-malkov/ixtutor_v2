from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_register', views.register, name='user_register'),
    path('user_login', views.login, name='user_login'),
    # path('tutor/Booking', views.tutorBooking, name='tutorBooking'),
    path('user/viewAllBookings', views.view_all_bookings, name='viewAllBookings')
]
