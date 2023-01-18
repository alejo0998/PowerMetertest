from mediciones.models import Medicion


class MedidorCalculo:
    def maximo(self, medidor):
        return Medicion.objects.filter(medidor=medidor).order_by('-consumo_registrado')[0].consumo_registrado

    def minimo(self, medidor):
        return Medicion.objects.filter(medidor=medidor).order_by('consumo_registrado')[0].consumo_registrado

    def total(self, medidor):
        return sum(Medicion.objects.filter(medidor=medidor).values_list('consumo_registrado', flat=True))

    def promedio(self, medidor):
        mediciones = Medicion.objects.filter(medidor=medidor)
        return sum(mediciones.values_list('consumo_registrado', flat=True))/len(mediciones)
