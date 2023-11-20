
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from cores.models import Machine
from django.db.models import Q 
import operator 

class RegisterMachine(APIView):

    @staticmethod
    def post(request, *args, **kwargs):
    
        rData = request.data
        if('name' in rData):
            print(rData['name'])
            machine_list = Machine.objects.filter(name=rData['name'])
            if(len(machine_list)==0):
                machine = Machine.objects.create(name=rData['name'])
                return Response({"machine_id":machine.id}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error":"Name already use"},status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)

