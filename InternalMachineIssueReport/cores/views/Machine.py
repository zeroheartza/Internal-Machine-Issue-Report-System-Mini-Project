
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from cores.models import Machine
from django.db.models import Q 
import operator 

class MachineAPIView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
    

        return Response({"machine_id":"1"}, status=status.HTTP_201_CREATED)

