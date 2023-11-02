from .serializers import AdotanteSerializer,DogSerializer
from .models import Adotante,Dog
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET']) # Get todos os Adotantes
def getAdotantes(request):
    adotante = Adotante.objects.all()                                      # Get all tasks from database
    serializer = AdotanteSerializer(adotante, many=True)                   # Convert to JSON (serialize)
    return Response(serializer.data, status=status.HTTP_200_OK)     # Return JSON to client

@api_view(['GET']) # Get todos os Dogs 
def getDogs(request):
    dog = Dog.objects.all()                                      # Get all tasks from database
    serializer = DogSerializer(dog, many=True)                   # Convert to JSON (serialize)
    return Response(serializer.data, status=status.HTTP_200_OK)     # Return JSON to client

@api_view(['POST']) # Criar um Adotante
def createAdotantes(request):
    serializer = AdotanteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
