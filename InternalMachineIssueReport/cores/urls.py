
from django.contrib import admin
from django.urls import path, include

from django.urls import path
from cores.views import Machine

urlpatterns = [
    path("/", Machine.MachineAPIView.as_view(), name="student_score"),

    path("register_machine/", Machine.MachineAPIView.as_view(), name="student_score"),
   
]
