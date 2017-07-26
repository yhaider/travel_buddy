from django.shortcuts import render, redirect
from django.contrib import messages
from models import Trip, TripManager, User, UserManager
from datetime import datetime

def home(request):
    if not 'user_id' in request.session:
        messages.add_message(request, messages.INFO, "You need to log in or register first.", extra_tags = 'login')
        return redirect('/')
    context = {
        'trips': User.objects.get(id=request.session['user_id']).trips.all(),
        'all_trips': Trip.objects.exclude(users = request.session['user_id'])
    }
    return render(request, 'trips/travels.html', context)
    # Displays all trips and separates them into two tables
    # depending on if the user is on the trip or not
    # Also does not allow anyone to proceed to the route
    # unless they have logged in


def add(request):
    if not 'user_id' in request.session:
        messages.add_message(request, messages.INFO, "You need to log in or register first.", extra_tags = 'login')
        return redirect('/')
    return render(request,'trips/add.html')
    # Simply renders the page for adding a trip
    # Also does not allow anyone to proceed to the route
    # unless they have logged in


def process(request):
    errors = Trip.objects.validator(request.POST)
    if len(errors):
        for tag,error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/travels/add')
    else:
        u = User.objects.get(id=request.session['user_id'])
        u.save()
        trip = Trip.objects.create(destination=request.POST['destination'], description=request.POST['description'], start_date = request.POST['start_date'], end_date = request.POST['end_date'], created_at = datetime.now(), updated_at = datetime.now())
        trip.save()
        trip.users.add(u)
        trip.save()
        return redirect('/travels')
    # If form data does not pass validations as
    # described in models.py for trips app
    # then user is shown errors
    # Otherwise, the trip is created and added
    # to the user's table which is displayed when it redirects


def destination(request, number):
    if not 'user_id' in request.session:
        messages.add_message(request, messages.INFO, "You need to log in or register first.", extra_tags = 'login')
        return redirect('/')
    trip = Trip.objects.get(id=number)
    context = {
        'destination': trip.destination,
        'description': trip.description,
        'start_date': trip.start_date,
        'end_date': trip.end_date,
        'planner': trip.users.first(),
        'all_users': trip.users.all()
    }
    return render(request, 'trips/destination.html', context)
    # Displays the information for the trip
    # with the number as its ID
    # Also does not allow anyone to proceed to the route
    # unless they have logged in


def join(request, number):
    trip = Trip.objects.get(id=number)
    trip.save()
    newuser = User.objects.get(id=request.session['user_id'])
    newuser.save()
    trip.users.add(newuser)
    return redirect('/travels')
    # Adds a user to the trip with an id that is the same number passed
    # in the url and shows that trip under that user's schedule tables
    # now instead


def leave(request, number):
    trip = Trip.objects.get(id=number)
    trip.save()
    user = User.objects.get(id=request.session['user_id'])
    trip.users.remove(user)
    if not trip.users.all():
        trip.delete()
    return redirect('/travels')
    # Removes a user from the trip with the id that is the same as the
    # number passed into the url and then redirects to the schedule page
    # to now display the trip under other user's trips OR it deletes the
    # trip if there are no other users going on it
