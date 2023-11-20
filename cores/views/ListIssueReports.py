
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from cores.models import Machine,Issue
from django.db.models import Q 
import operator 
from ..serializers import IssueSerializer
class ListIssueReports(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        page = request.GET.get('page',None)
        issue = Issue.objects.all().order_by('id') 
        if(page is not None):
            start = int(0)  if(int(page)==int(1)) else 5* (int(page) -1 )
            end = 5 * int(page)
            issue = issue[start:end]
        return Response(IssueSerializer(issue,many=True).data, status=status.HTTP_200_OK)
    