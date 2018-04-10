# Django-Celery-RabbitMQ
Integrando colas de tareas con Celery y RabbitMQ

# Aspectos a tener en cuenta
El proyecto ya cuenta con unos datos que fueron utilizados en un ambiente local cargados desde la API de jsonplaceholder estos datos fueron insertados de manera asincrona

1) crear el entorno virtual e instalar las dependencias necesarias del archivo requirements.txt 
2)Borre el archivo manage.py
3) ejecute el comando para correr las migraciones
4) desde la shell 
5) cargar el archivo de tasks.py desde la shell 
6) y ejecutar la siguiente linea: nombre_del_metodo.delay()
