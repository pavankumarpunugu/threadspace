
from django.urls import path
from . import views

urlpatterns=[
path("",views.home,name="home"),
path("like/<int:id>/",views.like_post,name="like"),
]
