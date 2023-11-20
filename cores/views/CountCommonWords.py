
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from cores.models import Machine,Issue
from django.db.models import Q 
import operator 
from ..serializers import IssueSerializer
import datetime
from django.db.models import Count
from ..util import get_top_k_common_words
class CountCommonWords(APIView):

    

    @staticmethod
    def get(request, *args, **kwargs):
        top_k = request.GET.get('top_k',None)
        issue =  Issue.objects.all()
        if(top_k is None):
            result = get_top_k_common_words(issue)
        else:
            result = get_top_k_common_words(issue,int(top_k))
        return Response(result, status=status.HTTP_200_OK)
    