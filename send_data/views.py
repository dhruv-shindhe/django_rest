from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import data_store
from .serializers import dataSerializer


# Create your views here.
class dataView(APIView):

    def get(self, request):
        data_all = data_store.objects.all()
        data_serilizer = dataSerializer(data_all,many=True)
        return Response(data_serilizer.data)

    def post(self, request, format=None):
        data_serilizer = dataSerializer(data=request.data)
        if data_serilizer.is_valid():
            data_serilizer.save()
            return Response(data_serilizer.data, status=status.HTTP_201_CREATED)
        return Response(data_serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
