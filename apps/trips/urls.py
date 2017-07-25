from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.home),

    url(r'^add$', views.add),

    url(r'^destination/(?P<number>\d+)$', views.destination),

    url(r'^process$', views.process),

    url(r'^join/(?P<number>\d+)$', views.join),

    url(r'^leave/(?P<number>\d+)$', views.leave)

]
