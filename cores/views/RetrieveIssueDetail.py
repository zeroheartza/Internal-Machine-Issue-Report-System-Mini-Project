
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from cores.models import Machine,Issue,History
from django.db.models import Q 
import operator 
from ..serializers import IssueSerializer,HistorySerializer

class RetrieveIssueDetail(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
     
        issue_id = kwargs.get("issue_id", None)
        if(issue_id is not None):
            rData = request.data
            try:
                issue = Issue.objects.get(id=int(issue_id))
            except Issue.DoesNotExist:  
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
            issueSerializer = IssueSerializer(issue).data
            history = []
            history_list = History.objects.filter(issue=issue)
            for his in history_list:
                data = {
                    "status": his.status,
                    "timestamp": his.timestamp,
                }
                if(his.comment is not None):
                    data['comment'] = his.comment
                history.append(data)

            issueSerializer["history"] = history
            
            return Response(issueSerializer, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

