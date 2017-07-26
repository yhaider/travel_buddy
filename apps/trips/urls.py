from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.home),
    # This is the route to the main travels
    # page that is accessed once the user
    # has logged in

    url(r'^add$', views.add),
    # This is the route that renders the page
    # to the form that allows a user to add
    # a new trip

    url(r'^destination/(?P<number>\d+)$', views.destination),
    # These are destination specific pages that are
    # accessed when the destination is clicked.
    # They display the trip information

    url(r'^process$', views.process),
    # This route takes the add form information
    # and adds it to the user's trip schedule

    url(r'^join/(?P<number>\d+)$', views.join),
    # This allows a user to join another user's
    # trip

    url(r'^leave/(?P<number>\d+)$', views.leave)
    # This allows a user to leave the trip

]
