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

def add(request):
    if not 'user_id' in request.session:
        messages.add_message(request, messages.INFO, "You need to log in or register first.", extra_tags = 'login')
        return redirect('/')
    return render(request,'trips/add.html')

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

def join(request, number):
    trip = Trip.objects.get(id=number)
    trip.save()
    newuser = User.objects.get(id=request.session['user_id'])
    newuser.save()
    trip.users.add(newuser)
    return redirect('/travels')

def leave(request, number):
    trip = Trip.objects.get(id=number)
    trip.save()
    user = User.objects.get(id=request.session['user_id'])
    trip.users.remove(user)
    if not trip.users.all():
        trip.delete()
    return redirect('/travels')
