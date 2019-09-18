from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.forms.models import model_to_dict
from .forms import RegisterForm
from .models import Users

bookings = [{
    'tutorID': 1,
    'bookingID': 20,
    'interestID': 30,
    'roomID': 40,
    'slotID': 50
},
    {
        'tutorID': 2,
        'bookingID': 30,
        'interestID': 40,
        'roomID': 50,
        'slotID': 60
    },
    {
        'tutorID': 3,
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
        form = RegisterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = Users(email=email, password=password, status=1)
            user.save()
            context = {'email': email, 'userID':  model_to_dict(user)['userID']}
            return render(request, 'ix_tutor/index.html', context)
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def login(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = Users.objects.get(email=email, password=password, status=1)
            except ObjectDoesNotExist:
                context = {'form': form}
                return render(request, 'registration/login.html', context)
            userID = model_to_dict(user)['userID']
            context = {'email': email, 'userID': userID}
            return render(request, 'user_types.html', context)
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'registration/login.html', context)


def view_all_bookings(request):
    return render(request, 'all_bookings.html', {"list": bookings})


def userType(request):
    return render(request, 'user_types.html')


def booking_information(request, bookingID):
    for booking in bookings:
        if booking['bookingID'] == bookingID:
            return render(request, 'booking_information.html', booking)