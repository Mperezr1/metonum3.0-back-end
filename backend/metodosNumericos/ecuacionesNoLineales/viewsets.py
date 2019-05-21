from rest_framework import viewsets
from .models import EcuacionesNoLineales
from .serializer import EcuacionesNoLinealesSerializer


class EcuacionesNoLinealesViewSet(viewsets.ModelViewSet):
    queryset = EcuacionesNoLineales.objects.all()
    serializer_class = EcuacionesNoLinealesSerializer
