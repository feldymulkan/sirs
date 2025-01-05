from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Pegawai
from .serializers import PegawaiSerializer

# List and Create Pegawai

class PegawaiList(APIView):
    def get(self, request):
        pegawaiList = Pegawai.objects.all()
        serializer = PegawaiSerializer(pegawaiList, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PegawaiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailPegawai(APIView):
    def get(self, request, pk):
        try:
            pegawai = Pegawai.objects.get(pk=pk)
        except:
            return Response({'error':'Pegawai tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PegawaiSerializer(pegawai)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            pegawai = Pegawai.objects.get(pk=pk)
        except:
            return Response({'error':'Pegawai tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PegawaiSerializer(pegawai, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            pegawai = Pegawai.objects.get(pk=pk)
        except Pegawai.DoesNotExist:
            return Response({'error':'Pegawai tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)
        pegawai.delete()
        return Response({'message': 'Pegawai deleted'}, status=status.HTTP_204_NO_CONTENT)
    
    