
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from cores.models import Machine,Issue
from django.db.models import Q 
import operator 
from ..serializers import IssueSerializer
import datetime
from django.db.models import Count

class CountingIssueReports(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        page = request.GET.get('page',None)
        issue =  Issue.objects.values('machine').annotate(num_machine=Count('machine')).order_by('-num_machine')
        arr_data = []
        machine_have_issue = []
        for i in issue:       
            data = {
                "machine_id": i['machine'],
                "issue_count": i['num_machine']
            }
            machine_have_issue.append(i['machine'])
            arr_data.append(data)
        
        machine = Machine.objects.filter(~Q(id__in=machine_have_issue)).order_by('id')

        for i in machine:
            data = {
                "machine_id": i.id,
                "issue_count": 0
            }
            arr_data.append(data)
        
        if(page is not None):
            start = int(0)  if(int(page)==int(1)) else 5* (int(page) -1 )
            end = 5 * int(page)
            arr_data = arr_data[start:end]
        return Response(arr_data, status=status.HTTP_200_OK)
    