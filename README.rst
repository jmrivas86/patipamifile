Channels is coming - PyConES16
==============================

Este repositorio contiene el código de la demo creada para la charla "Channels is coming: real-time web in Django" presentada en la pycones 2016.

PatiPamiFile es una prueba de concepto de aplicación real en Django utilizando websockets integrando django-channels.

La aplicación es un sistema muy simple para compartir archivos.


Instalación
------------

Insalación Manual
~~~~~~~~~~~~~~~~~~~~~~

Crea un nuevo virtualenv para el proyecto, y ejecuta::

    pip install -r requirements.txt

Necesitarás un redis corriendo en local; el settings del redis está configurado en ``localhost``, port ``6379``, podrás cambiar esto en el setting ``CHANNEL_LAYERS`` de ``settings.py``.

Finalmente, ejecuta::

    python manage.py migrate
    python manage.py runserver

Instalación con Docker
~~~~~~~~~~~~~~~~~~~~~~

Ejecuta la app::

    docker-compose up -d

La app estará levantada en: {docker-ip}:8000


*Notas:*

* Puede crear un superusuario con el comando createsuperuser.

    python manage.py createsuperuser

* Para registrar usuarios puede utilizar la zona de administración de Django.
* Los carpetas (Box) que se creen no se verán reflejados en tiempo real, la prueba de concepto es sólo para los ficheros (filebox).
