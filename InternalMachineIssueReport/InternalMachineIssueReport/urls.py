
from django.contrib import admin
from django.urls import path, include
from cores.views import Machine

urlpatterns = [
path('admin/', admin.site.urls),
path('cores/', include('cores.urls')),
path("/", Machine.MachineAPIView.as_view(), name="student_score"),
path("", Machine.MachineAPIView.as_view(), name="student_score"),
]
