from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from . import models

bookings = [{
            'tutorID' : 1,
            'bookingID' : 20, 
            'interestID' : 30,
            'roomID' : 40, 
            'slotID' : 50
        },
        {
            'tutorID' : 2,
            'bookingID': 30,
            'interestID': 40,
            'roomID': 50, 
            'slotID': 60
        },
        {
            'tutorID' : 3,
            'bookingID': 15,
            'interestID': 25,
            'roomID': 35, 
            'slotID': 45
        }]

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