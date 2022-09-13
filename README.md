# Introducción a MLOps
Este repositorio incluye el código utilizado en el webinar "MLOps en la práctica" que he impartido para el área de Big Data & Business Intelligence de la Universidad de Deusto. 

Este tutorial supone que la persona tiene conocimientos previos de:

* Google Cloud. Sobre todo de Cloud Run y el Container Registry ([enlace](https://anderfernandez.com/blog/como-poner-modelo-de-python-en-produccion/)).
* Docker ([enlace](https://anderfernandez.com/blog/docker-para-data-science/)).
* Control de versiones mediante Github.
* Python en general y en especial el framework FastAPI ([enlace](https://anderfernandez.com/blog/tutorial-sklearn-machine-learning-python/)) y Sklearn ([enlace](https://anderfernandez.com/blog/tutorial-sklearn-machine-learning-python/)).
* Aunque no usaremos Github Actions, creo que conocerlo te vendrá muy bien para saber encajar piezas ([enlace](https://anderfernandez.com/blog/github-actions-para-data-science/)).


## Introducción al caso de Uso
Para ver cómo funciona el nivel 1 de MLOps en la práctica, vamos a coger un caso de uso  *dummy*, de tal forma que lo importante no sea el código en sí, sino entender el proceso.

Para ello, he entrenado un modelo dummy que predice el tipo de planta Iris en función del ancho y alto del pétalo y sépalo. Además, he creado una API con FastAPI que recibe peticiones GET  y devuelve la predicción del modelo. 

## Pasos para el despliegue automatizado del modelo

1. **Entrenamiento del modelo**. Primero de todo se entrena el modelo y se guardan tanto el modelo como el transformador de datos en un fichero `.pickle` o similar. Este paso es realizado en el script `src/train.py`.

2. **Creación de una API para exponer el modelo**. Muchos modelos se exponen mediante para poder obtener la respuesta en el momento. En este caso, hemos creado una API con FastAPI que recibe los inputs del modelo y devuelve la predicción. Este fichero se puede encontrar en `api/api.py`.

3. **Creación del Docker**. Una vez comprobado que la API funciona se debe dockerizar. Esto se realiza con el fichero `Dockerfile`, el cual expone la API en el puerto 8080. 

> Es importante recordar el puerto, puesto que a la hora de desplegar el servicio en Cloud se tendrá que indicar que apunte al mismo puerto al que la aplicación escucha.

4. **Subida del Docker a Cloud y despliegue en Cloud Run**: usando el SDK de Google Cloud hacemos el *push* de la imagen al Container Registry (o Artifact Registry) y desplegamos la imagen en Cloud Run (también podría ser en K8s).

5. 


