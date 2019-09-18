# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Departments(models.Model):
    deptID = models.PositiveIntegerField(
        primary_key=True,
        null=False,
        editable=False
    )
    name = models.TextField(
        max_length=255
    )
    def __str__(self):
        return 'Dept ID:' + str(self.deptID)

class Interests(models.Model):

    interestID = models.PositiveIntegerField(
        primary_key=True,
        null=False,
        editable=False
    )
    name = models.TextField(
        max_length=255
    )
    def __str__(self):
        return 'Interest ID:' + str(self.interestID)

class Rooms(models.Model):
    roomID = models.PositiveIntegerField(
        primary_key=True,
        null=False,
        editable=False
    )
    name = models.TextField(
        max_length=255
    )
    def __str__(self):
        return 'Room ID:' + str(self.roomID)

class TimeSlots(models.Model):
    timeSlotID = models.PositiveIntegerField(
        primary_key=True,
        null=False,
        editable=False
    )
    name = models.TextField(
        max_length=255
    )
    def __str__(self):
        return 'Time Slot ID:' + str(self.timeSlotID)

class Days(models.Model):
    dayID = models.PositiveIntegerField(
        primary_key=True,
        null=False,
        editable=False
    )
    name = models.TextField(
        max_length=255
    )
    def __str__(self):
        return 'Day ID:' + str(self.dayID)

class Availability(models.Model):
    YES = 1
    NO = 0
    ANSWER = (
        (NO, 'No'),
        (YES, 'Yes')
    )

    bookingID = models.PositiveIntegerField(
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
    def __str__(self):
        return 'Day ID:' + str(self.dayID)

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

    userID = models.PositiveIntegerField(
        primary_key=True,
        null=False,
        editable=False
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
    deptID = models.ForeignKey(
        Departments,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return 'refers to departments reference:' + self.Departments.deptID

class UserInterests(models.Model):
        userID = models.ForeignKey(
            'Users',
            on_delete=models.CASCADE
        )
        interestID = models.ForeignKey(
            'Interests',
            on_delete=models.CASCADE
        )
        def __str__(self):
            return 'refers to departments reference:' + self.Interests.interestID + self.Users.userID

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
        def __str__(self):
            return 'refers to Availability reference:' + self.Interests.interestID + self.Users.userID + self.Availability.bookingID

class StudentEnroll(models.Model):
        userID = models.ForeignKey(
            'Users',
            on_delete=models.CASCADE
        )
        enrollID = models.ForeignKey(
            'Availability',
            on_delete=models.CASCADE
        )
        def __str__(self):
            return 'refers to Availability reference:' + self.Users.userID + self.Availability.bookingID
