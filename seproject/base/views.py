from django.shortcuts import render
from rest_framework import viewsets
from .models import EntryExitRecord
from .serializers import EntryExitRecordSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.

class EntryExitRecordViewSet(viewsets.ModelViewSet):
    queryset = EntryExitRecord.objects.all()
    serializer_class = EntryExitRecordSerializer

    @action(detail=True, methods=['post'])
    def enter(self, request, pk=None):
        employee = self.get_object()
        employee.enter()
        return Response(status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def exit(self, request, pk=None):
        employee = self.get_object()
        employee.exit()
        return Response(status=status.HTTP_200_OK)