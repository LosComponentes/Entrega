# Integrantes:

- Maria Alejandra Estrada Garcia 
- Ana Sofía Padilla Daza 
- Ever Martínez
- Eduar Romero
- Valeria Caro Ramirez


# Entrega 4

Para la entrega 4 no vamso a tener enlace de wiki sino todo se va a escribir en este readme. 

## Video



## Microservicios

- Imagen
- Metadata
- Anonimización
- Script

## Escenario de prueba 

### Escenario 1: Seguridad - Anonimización de los datos en Data Partneship 

![Template escenario 1 seguridad](https://github.com/user-attachments/assets/33ee9214-4f93-485e-b8ca-e79dc5040c4b)

![Diagrama Escenario 1](https://github.com/user-attachments/assets/17ef3a0f-982a-4262-b782-178a998d06cf)
[Diagrama Escenario 1](https://github.com/user-attachments/assets/17ef3a0f-982a-4262-b782-178a998d06cf)

### Escenario 2: Adaptarse a requisitos de protección de datos de un nuevo país

![Template Escenario](https://github.com/user-attachments/assets/01ada5a9-b0bc-44df-8dc1-13f877315b13)

![Diagrama Funcional C C](https://github.com/user-attachments/assets/7db70ee0-0a66-45f9-b3d4-06888b2ad281)
[Diagrama Escenario 2](https://github.com/user-attachments/assets/7db70ee0-0a66-45f9-b3d4-06888b2ad281)

### Escenario 3: Escalabilidad en ejecución de script de eliminación de datos sensibles (anonimización)

![Template Escenario](https://github.com/user-attachments/assets/0cdbe1e1-4de3-4dff-88f7-dbefe4b02d51)

![Diagrama](https://github.com/user-attachments/assets/5b8821ba-f832-4bab-a909-6eb2af279801)
[Diagrama](https://github.com/user-attachments/assets/5b8821ba-f832-4bab-a909-6eb2af279801)

### Justificación implementación

Se implementaron los microservicios anteriormente descritos basandose en este diagrama:

![Diagrama entrega 4](https://github.com/user-attachments/assets/017645e6-2a90-4b77-b9e9-a8559b14dff1)


# Entrega 3

## Wiki

Este es el [enlace entrega 3](https://github.com/LosComponentes/Entrega-3/wiki/Entrega-3) a la wiki del proyecto donde se encuentra también información de la entrega como son los escenarios de calidad, siguiendo el template presentado en la entrega.

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


## Video

[Video](https://uniandes-my.sharepoint.com/:v:/g/personal/m_estradag_uniandes_edu_co/ESe8Sk8jrXdKiHhW0nMQyqIBOTfF5pD1PBrWsawZXCB05Q?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=2Tkd8F )

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
