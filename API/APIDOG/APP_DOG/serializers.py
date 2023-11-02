from rest_framework import serializers
from .models import Adotante,Dog

class AdotanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adotante
        fields = '__all__' # All fields of model


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__' # All fields of model