from rest_framework import serializers, fields

from mediciones.models import Medicion, Medidor


class MedidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medidor
        fields = '__all__'


class MedicionSerializer(serializers.ModelSerializer):
    fecha_hora = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Medicion
        fields = ('id', 'medidor', 'fecha_hora', 'consumo_registrado')