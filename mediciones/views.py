from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from mediciones.helpers import MedidorCalculo
from mediciones.models import Medicion, Medidor
from mediciones.serializer import MedicionSerializer, MedidorSerializer
from rest_framework import status
from rest_framework.response import Response


class MedidorViewSet(ModelViewSet):
    queryset = Medidor.objects.all()
    serializer_class = MedidorSerializer

    def get_queryset(self):
        return super().get_queryset()



@api_view(["GET"])
def medidor_maximo(request, pk):
    try:
        medidor = Medidor.objects.get(id=pk)
        return Response(MedidorCalculo().maximo(medidor), status.HTTP_200_OK)
    except Exception as e:
        return Response(e, status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def medidor_minimo(request, pk):
    try:
        medidor = Medidor.objects.get(id=pk)
        return Response(MedidorCalculo().minimo(medidor), status.HTTP_200_OK)
    except Exception as e:
        return Response(e, status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def medidor_promedio(request, pk):
    try:
        medidor = Medidor.objects.get(id=pk)
        return Response(MedidorCalculo().promedio(medidor), status.HTTP_200_OK)
    except Exception as e:
        return Response(e, status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def medidor_total(request, pk):
    try:
        medidor = Medidor.objects.get(id=pk)
        return Response(MedidorCalculo().total(medidor), status.HTTP_200_OK)
    except Exception as e:
        return Response(e, status.HTTP_404_NOT_FOUND)

class MedicionViewSet(ModelViewSet):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer
