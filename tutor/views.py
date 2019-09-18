from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from . import models

bookings = [{
            'tutorID' : 1,
            'bookingID' : 1, 
            'interestID' : 1,
            'roomID' : 3, 
            'slotID' : 2
        },
        {
            'tutorID' : 2,
            'bookingID': 2,
            'interestID': 2,
            'roomID': 2, 
            'slotID': 2
        },
        {
            'tutorID' : 3,
            'bookingID': 3,
            'interestID': 1,
            'roomID': 3, 
            'slotID': 1
        }]


interests = [{
    'interestID' : 1,
    'name' : "Identity"
    },
    {
    'interestID' : 2,
    'name' : "Python"
    },
    {
    'interestID' : 3,
    'name' : "Wrapper"
    }
]

rooms = [{
    'roomID' : 1,
    'name' : "Room A"
    },
    {
    'roomID' : 2,
    'name' : "Room B"   
    },
    {
    'roomID' : 3,
    'name' : "Room C"   
    }
]

timeSlots = [{
    'timeSlotID' : 1,
    'name' : '10AM-11AM'
    },
    {
    'timeSlotID' : 2,
    'name' : '2PM-3PM'
    },
    {
    'timeSlotID' : 3,
    'name' : '12PM-1PM'
    }
]

days = [{
    'dayID' : 1,
    'name' : "Monday"
    },
    {
    'dayID' : 2,
    'name' : "Wednesday"
    },
    {
    'dayID' : 1,
    'name' : "Friday"
    }
]

availability = [{
    'bookingID' : 1,
    'isAvailable' : 1,
    'dayID' : 1,
    'roomID' : 2,
    'timeSlotID' : 3
    },
    {
    'bookingID' : 2,
    'isAvailable' : 1,
    'dayID' : 1,
    'roomID' : 2,
    'timeSlotID' : 2
    },
    {
    'bookingID' : 3,
    'isAvailable' : 0,
    'dayID' : 3,
    'roomID' : 2,
    'timeSlotID' : 1
    }
]

users = [{
    'userID' : 1,
    'email' : 'email1@gmail.com',
    'status' : 1,
    'password' : "password",
    'isTutor' : 0,
    'isStudent': 0,
    },
    {
    'userID' : 2,
    'email' : 'email2@gmail.com',
    'status' : 0,
    'password' : "password",
    'isTutor' : 1,
    'isStudent': 0,
    },
    {
    'userID' : 3,
    'email' : 'email3@gmail.com',
    'status' : 1,
    'password' : "password",
    'isTutor' : 0,
    'isStudent': 1,
    }
]

userInterests = [{
    'userID' : 1,
    'interestID' : 1 
    },
    {
    'userID' : 2,
    'interestID' : 2
    },
    {
    'userID' : 3,
    'interestID' : 3 
    }
]

tutorBookings = [{
    'bookingID' : 1,
    'userID' : 1,
    'interestID' : 1
    },
    {
    'bookingID' : 1,
    'userID' : 3,
    'interestID' : 2
    },
    {
    'bookingID' : 1,
    'userID' : 2,
    'interestID' : 3
    }
]

studentEnroll = [{
    'userID' : 1,
    'enrollID' : 2
    },
    {
    'userID' : 3,
    'enrollID' : 1
    },
    {
    'userID' : 2,
    'enrollID' : 3
    }
]

# Create your views here.
def index(request):
    return render(request, 'ix_tutor/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def view_all_bookings(request):
    return render(request, 'all_bookings.html', {"list" : bookings})


def booking_information(request, bookingID):
    for booking in bookings:
        if booking['bookingID'] == bookingID:
            return render(request, 'booking_information.html', booking)

'''
def tutor_create_booking(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'tutor_bookings.html', context)
'''

def view_created_bookings(userID):
    createdBookings = []
    for booking in bookings:
        if booking['tutorID'] == userID:
            createdBookings.append(booking)
    return createdBookings

