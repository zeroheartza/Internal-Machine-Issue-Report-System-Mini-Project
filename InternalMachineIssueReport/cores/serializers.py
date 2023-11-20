from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import *
from .models import Machine,Issue,History

class MachineSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Machine
        fields = '__all__'

class IssueSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Issue
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = History
        fields = '__all__'