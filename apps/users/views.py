from django.shortcuts import render, redirect
from django.contrib import messages
from models import User, UserManager
import bcrypt

def routetomain(request):
    return redirect('/main')

def index(request):
    return render(request, 'users/index.html')
    # Simply renders the template for login/registration forms

def login(request):
    errors = User.objects.loginvalidator(request.POST)
    if len(errors):
        for tag,error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        request.session['name'] = User.objects.get(email=request.POST['email']).first_name
        request.session['user_id'] = User.objects.get(email=request.POST['email']).id
        return redirect('/travels')
    # If there are errors, they will display as dismissable alerts
    # on the homepage, otherwise it will proceed and login in the user

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag,error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
    else:
        pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], email = request.POST['email'], password = pwhash)
        request.session['name'] = request.POST['fname']
        request.session['user_id'] = user.id
        messages.add_message(request, messages.INFO, "Welcome aboard, {}! This is your travel dashboard where you can plan your own trips and join other trips. Safe travels!".format(request.session['name']), extra_tags='newcomer')
        return redirect('/travels')
    return redirect('/')
    # If there are errors, they will display as dismissable alerts
    # on the homepage, otherwise it will proceed, add, and welcome the user

def logout(request):
    request.session.clear()
    messages.add_message(request, messages.INFO, "You have been logged out.", extra_tags='logout')
    return redirect('/')
