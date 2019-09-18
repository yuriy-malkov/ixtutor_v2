from django.db import models


# Create your models here.

class Departments(models.Model):
    deptID = models.AutoField(
        primary_key=True,
        null=False,
        editable=False
    )
    name = models.TextField(
        max_length=255
    )


class Interests(models.Model):
    interestID = models.AutoField(
        primary_key=True,
        null=False,
        editable=False
    )
    name = models.TextField(
        max_length=255
    )


class Rooms(models.Model):
    roomID = models.AutoField(
        primary_key=True,
        null=False,
        editable=False
    )
    name = models.TextField(
        max_length=255
    )


class TimeSlots(models.Model):
    timeSlotID = models.AutoField(
        primary_key=True,
        null=False,
        editable=False
    )
    name = models.TextField(
        max_length=255
    )


class Days(models.Model):
    dayID = models.AutoField(
        primary_key=True,
        null=False,
        editable=False
    )
    name = models.TextField(
        max_length=255
    )


class Availability(models.Model):
    YES = 1
    NO = 0
    ANSWER = (
        (NO, 'No'),
        (YES, 'Yes')
    )

    bookingID = models.AutoField(
        primary_key=True,
        null=False,
        editable=False
    )
    isAvailable = models.PositiveIntegerField(
        choices=ANSWER,
        default=1
    )
    dayID = models.ForeignKey(
        'Days',
        on_delete=models.CASCADE
    )
    roomID = models.ForeignKey(
        'Rooms',
        on_delete=models.CASCADE
    )
    timeSlotID = models.ForeignKey(
        'TimeSlots',
        on_delete=models.CASCADE
    )


class Users(models.Model):
    ACTIVE = 1
    DEACTIVE = 2
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEACTIVE, 'Deactive')
    )

    YES = 1
    NO = 0
    OCCUPATION = (
        (NO, 'No'),
        (YES, 'Yes')
    )

    userID = models.AutoField(
        primary_key=True,
        null=False
    )
    email = models.EmailField(
        max_length=30,
        default=''
    )
    status = models.SmallIntegerField(
        choices=STATUS_CHOICES
    )
    password = models.TextField(
        max_length=255
    )
    isTutor = models.PositiveIntegerField(
        choices=OCCUPATION,
        default=0
    )
    isStudent = models.PositiveIntegerField(
        choices=OCCUPATION,
        default=0
    )


class UserInterests(models.Model):
    userID = models.ForeignKey(
        'Users',
        on_delete=models.CASCADE
    )
    interestID = models.ForeignKey(
        'Interests',
        on_delete=models.CASCADE
    )


class TutorBookings(models.Model):
    bookingID = models.ForeignKey(
        'Availability',
        on_delete=models.CASCADE
    )
    userID = models.ForeignKey(
        'Users',
        on_delete=models.CASCADE
    )
    interestID = models.ForeignKey(
        'Interests',
        on_delete=models.CASCADE
    )


class StudentEnroll(models.Model):
    userID = models.ForeignKey(
        'Users',
        on_delete=models.CASCADE
    )
    enrollID = models.ForeignKey(
        'Availability',
        on_delete=models.CASCADE
    )