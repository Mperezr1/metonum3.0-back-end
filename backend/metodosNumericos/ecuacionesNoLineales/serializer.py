from rest_framework import serializers
from .models import EcuacionesNoLineales


class EcuacionesNoLinealesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcuacionesNoLineales
        fields = '__all__'
