# Entrega-3

## Integrantes:

- Maria Alejandra Estrada Garcia 
- Ana Sofía Padilla Daza 
- Ever Martínez
- Eduar Romero
- Valeria Caro Ramirez

## Wki

Este es el [enlace](https://github.com/LosComponentes/Entrega-3/wiki/Entrega-3) a la wiki del proyecto donde se encuentra también información de la entrega como son los escenarios de calidad, siguiendo el template presentado en la entrega.

## Diagrama

El servicio que se va a implementar es de la imágenes médicas y sus metadatos, que se encuentra dentro de este diagrama (agregación de imágen).

![VistaInformacionFlujoObtenerDatos-New drawio (1)](https://github.com/user-attachments/assets/7d49cc59-c67b-4996-88ff-d8e45ff55e86)

## Estructura del proyecto 

El proyecto SaludTech de los Alpes está organizado siguiendo una arquitectura de microservicios y Domain-Driven Design (DDD). Se divide en tres capas principales: Aplicación, dominio, e infraestructura

El módulo que impelmentamos fue el manejador_datos (imágenes)/ → Es el microservicio encargado de gestionar imágenes médicas y sus metadatos. Está dividido en tres módulos principales:

- Aplicacion/ → Contiene la lógica de negocio, comandos, queries y mapeadores.
- Dominio/ → Define las entidades, objetos de valor, reglas de negocio y eventos de dominio.
- Infraestructura/ → Gestiona la persistencia, integración con otros sistemas y comunicación con eventos.

[Diagrama](https://github.com/user-attachments/assets/14066409-a023-4bf5-a386-6f1891dca8f9)

El módulo aplicacion/comandos/ y aplicacion/queries/ implementa CQRS (Command Query Responsibility Segregation) para separar las operaciones de escritura y lectura. Esto permite un mejor rendimiento y escalabilidad en el sistema.

Por ejemplo, el archivo agregar_imagen.py maneja la creación de imágenes médicas, mientras que consultar_imagen.py permite recuperarlas sin modificar su estado.

El archivo dominio/eventos.py define eventos de dominio que notifican cambios en el sistema. Un caso clave es ImagenCreada, que se dispara cuando se registra una nueva imagen médica.

Dentro de infraestructura/, los archivos consumidores.py y despachadores.py gestionan la comunicación con un broker de eventos. Los consumidores reciben imágenes médicas anonimizadas, mientras que los despachadores envían eventos de integración a otros servicios.

El directorio infraestructura/schema/ define los esquemas de eventos y comandos. Se usa un formato versionado (schema/v1/...) para mantener compatibilidad con futuras actualizaciones.

En el seedwork, los archivos comandos.py y queries.py proporcionan una base estándar para manejar comandos y consultas en el sistema. Esto garantiza coherencia en la lógica de negocio.


## Saludtech
### Ejecutar Aplicación

Desde el directorio principal ejecute el siguiente comando.

```bash
flask --app src/saludtech/api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
flask --app src/saludtech/api --debug run
```

### Ejecutar pruebas

```bash
coverage run -m pytest
```

### Ver reporte de covertura
```bash
coverage report
```

### Crear imagen Docker

Desde el directorio principal ejecute el siguiente comando.

```bash
docker build . -f saludtech.Dockerfile -t aeroalpes/flask
```

### Ejecutar contenedora (sin compose)

Desde el directorio principal ejecute el siguiente comando.

```bash
docker run -p 5000:5000 saludtech/flask
```
