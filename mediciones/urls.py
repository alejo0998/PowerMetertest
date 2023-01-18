from django.urls import path

from mediciones.views import MedicionViewSet, MedidorViewSet, medidor_maximo, medidor_minimo, medidor_promedio, medidor_total


urlpatterns = [
    path('medidores', MedidorViewSet.as_view({'get': 'list', 'post': 'create'}), name='medidor-list-create'),
    path('medidores/<int:pk>', MedidorViewSet.as_view({'get': 'retrieve'}), name='medidor-retrieve'),
    path('medidores/<int:pk>/maximo', medidor_maximo, name='medidor-retrieve-maximo'),
    path('medidores/<int:pk>/minimo', medidor_minimo, name='medidor-retrieve-minimo'),
    path('medidores/<int:pk>/total', medidor_total, name='medidor-retrieve-total'),
    path('medidores/<int:pk>/promedio', medidor_promedio, name='medidor-retrieve-promedio'),
    path('mediciones', MedicionViewSet.as_view({'get': 'list', 'post': 'create'}), name='medicion-list-create'),
    path('mediciones/<int:pk>', MedicionViewSet.as_view({'get': 'retrieve'}), name='medicion-retrieve'),

]