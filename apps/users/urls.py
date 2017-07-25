from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.routetomain),
    # Navigates to homepage
    # where there are login
    # and registration forms

    url(r'^main$', views.index),
    # Also navigates to homepage

    url(r'^login$', views.login),
    # Processes login with validations
    # Either proceeds to next page or
    # displays messages as dismissable alerts

    url(r'^register$', views.register),
    # Processes registration with validations
    # Either proceeds to next page or
    # displays messages as dismissable alerts

    url(r'^logout$', views.logout)
    # Logs the user out
]
