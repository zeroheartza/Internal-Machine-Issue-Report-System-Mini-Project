
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from cores.models import Machine,Issue
from django.db.models import Q 
import operator 
class ReportIssue(APIView):

    @staticmethod
    def post(request, *args, **kwargs):
    
        rData = request.data
        if(('machine_id' in rData) and ('issue' in rData) and ('description' in rData)):
           
            issue = Issue.objects.create(
                machine_id=rData['machine_id'],
                issue=rData['issue'],
                description=rData['description']
            )
            print(issue)
            return Response({"issue_id":issue.id}, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

