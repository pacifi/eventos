# Sistema de Inscripción


Sistema de inscripción para el registro de estudiantes a cursos desarrollado para `desarrolloglobal`

## Proceso de desarrollo.

Modulo Inicial fase de pruebas. administracion via django admin

## Proceso Terminado.

Conección a API REST, Registro de Eventos  

## Modulos

1. Registro de Eventos
2. Registro de AccesToken.
3. Lista de eventos.
4. Registro incripción.
5. Validación de pago via rest

## Dependencias del sistema.

1. Python 3

## Ejecución

    $ git clone https://github.com/pacifi/eventos.git
    $ cd eventos
    $ virtualenv -p python3 venv
    $ source venv/bin/activate  # Linux
    $ source venv/bin/Scripts/activate # Windows
    $ pip install -r requirements.txt
    $ python manage.py makemigrations 
    $ python manage.py migrate
    $ python manage.py loaddata data.json
    $ python manage.py runserver 8000
    
Visitar la página de Inicio http://localhost:8000


    
