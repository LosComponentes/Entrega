# Entrega-3

## Integrantes:

- Maria Alejandra Estrada Garcia 
- Ana Sofía Padilla Daza 
- Ever Martínez
- Eduar Romero
- Valeria Caro Ramirez

## Wki

Este es el [enlace](https://github.com/LosComponentes/Entrega-3/wiki/Entrega-3) a la wiki del proyecto donde se encuentra también información de la entrega como son los escenarios de calidad, siguiendo el template presentado en la entrega.

## Implementación

El servicio que se va a implementar es de la imágenes médicas y sus metadatos, que se encuentra dentro de este diagrama (agregación de imágen).

![VistaInformacionFlujoObtenerDatos-New drawio (1)](https://github.com/user-attachments/assets/7d49cc59-c67b-4996-88ff-d8e45ff55e86)

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
