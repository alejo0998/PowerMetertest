Para inicializar el proyecto:
1) Clonar el repositorio.
2) Dentro de la carpeta PowerMeterDesafio ejecutar source venv/bin/activate.
3) Ejecutar python manage.py migrate para correr migraciones.
4) Ejecutar python manage.py runserver para dejar corriendo el servidor.

Ejercicio 1.

Subi una collection postman, con los endpoints.
Actualmente existen estos endpoints
'api/medidores' -> GET (list), POST
'api/medidores/<int:pk>' -> GET
'api/medidores/<int:pk>/maximo' -> GET
'api/medidores/<int:pk>/minimo' -> GET
'api/medidores/<int:pk>/total' -> GET
'api/medidores/<int:pk>/promedio' -> GET
'api/mediciones/' -> GET (list), POST
'api/mediciones/<int:pk>' -> GET
 
 Que resuelven lo solicitado en el ejercicio.
 Respecto a decisiones de diseño, al ser simplificado, no incorpore autenticacion, tambien si no seria un dominio simplificado, 
 agregaria test automatizados para testear la api.
 A su vez, el enunciado solicitaba que agregue endpoints para esas acciones, los agregue como solicito el enunciado, pero quizas en otro escenario sea util que maximo, minimo, total y promedio vengan cuando se le pega a api/medidores/<ID>, en este caso lo agregaria al
 serializer para que venga todo junto, y el cliente pueda consultar todo con un solo llamado, para evitar pegarle varias veces al servidor.
 Otra decision de diseño que tome, modifique el serializer para enviarle la fecha y hora en el formato '%Y-%m-%d %H:%M:%S', desde la collection postman esto se puede ver en el post.
 
 Ejercicio 2.
 Esta resuelto en un archivo dentro de este proyecto, para ejecutarlo hay que correr python ejercicio2.py, donde printee los resultados de cada item, y deje comentarios en el archivo.
