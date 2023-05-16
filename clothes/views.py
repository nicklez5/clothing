from pstats import Stats, StatsProfile
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *

class MenShirtAPIView(APIView):
    def get(self,request,format=None):
        shirts = Men_Shirt.objects.all()
        serializer = MenShirtSerializer(shirts,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = MenShirtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    def put(self,request,id=None):
        shirts = Men_Shirt.objects.filter(id=id)
        serializer = MenShirtSerializer(shirts,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        shirts = Men_Shirt.objects.filter(id=id)
        shirts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class MenShirtDetailAPIView(APIView):
    def get(self,request,id=None):
        shirts = Men_Shirt.objects.filter(id=id)
        serializer = MenShirtSerializer(shirts,many=True)
        return Response(serializer.data)
    
class MenJacketAPIView(APIView):
    def get(self,request,format=None):
        Jacket = Men_Jacket.objects.all()
        serializer = MenJacketSerializer(Jacket,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = MenJacketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    def put(self,request,id=None):
        Jackets = Men_Jacket.objects.filter(id=id)
        serializer = MenJacketSerializer(Jackets,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        shirts = Men_Jacket.objects.filter(id=id)
        shirts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class MenJacketDetailAPIView(APIView):
    def get(self,request,id=None):
        Jackets = Men_Jacket.objects.filter(id=id)
        serializer = MenJacketSerializer(Jackets,many=True)
        return Response(serializer.data)

class MenPantsAPIView(APIView):
    def get(self,request,format=None):
        Pantss = Men_Pants.objects.all()
        serializer = MenPantsSerializer(Pantss,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = MenPantsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    def put(self,request,id=None):
        Pantss = Men_Pants.objects.filter(id=id)
        serializer = MenPantsSerializer(Pantss,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id=None):
        shirts = Men_Pants.objects.filter(id=id)
        shirts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class MenPantsDetailAPIView(APIView):
    def get(self,request,id=None):
        Pantss = Men_Pants.objects.filter(id=id)
        serializer = MenPantsSerializer(Pantss,many=True)
        return Response(serializer.data)
    
# Create your views here.
