
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from cores.models import Machine,Issue
from django.db.models import Q 
import operator 
from ..serializers import IssueSerializer
import datetime
class FilterIssueReports(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        machine_id = request.GET.get('machine_id',None)
        title = request.GET.get('title',None)
        description = request.GET.get('description',None)
        start_timestamp = request.GET.get('start_timestamp',None)
        end_timestamp = request.GET.get('end_timestamp',None)
        r_status = request.GET.get('status',None)
        print(type(start_timestamp))
        issue = Issue.objects.all().order_by('id') 

        if(machine_id is not None):
            issue = issue.filter(machine_id=machine_id)
        
        if(start_timestamp is not None):
            issue = issue.filter(timestamp__gte=start_timestamp)
        
        if(end_timestamp is not None):
            end_timestamp = datetime.datetime.strptime(str(end_timestamp), '%Y-%m-%d') + datetime.timedelta(days=1)
            issue = issue.filter(timestamp__lte=end_timestamp)
        
        if(r_status is not None):
            issue = issue.filter(status=r_status)      

        if(title is not None):
            issue = list(filter(lambda x: (title in x.issue ), issue)) 
 
        if(description is not None):
            issue = list(filter(lambda x: (description in x.description ), issue))   
       
        return Response(IssueSerializer(issue,many=True).data, status=status.HTTP_200_OK)
    