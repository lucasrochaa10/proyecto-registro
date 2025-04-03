# Proyecto de Registro de Asistentes

Este proyecto permite registrar asistentes mediante un formulario web desarrollado en Angular. Los datos se almacenan en una base de datos Firestore (Google Cloud) a través de una API creada con FastAPI. El backend está desplegado en Cloud Run utilizando Docker.

## Tecnologías utilizadas

- **Frontend:** Angular
- **Backend:** FastAPI (Python)
- **Base de datos:** Firestore (Google Cloud)
- **Despliegue del backend:** Docker + Cloud Run (Google Cloud)
- **Control de versiones:** Git + GitHub

## Funcionalidades

- Registro de asistentes con los siguientes campos:
  - Nombre completo
  - DNI o NIE (validados con expresiones regulares)
  - Email (validado)
  - Fecha de nacimiento
- Almacenamiento de los datos en Firestore
- Listado de asistentes registrados
- Paginación para navegar por los registros
- Validación en frontend y backend
- Despliegue del backend en la nube (accesible desde el frontend)

## URL del backend desplegado

[https://backend-app-573298363717.europe-west1.run.app](https://backend-app-573298363717.europe-west1.run.app)

## Cómo ejecutar el proyecto localmente

### Backend (FastAPI)

```bash
cd web_registro
uvicorn main:app --reload

cd frontend-registro
ng serve

proyecto-registro/
├── frontend-registro/   # Angular (formulario, estilos y paginación)
└── web_registro/        # FastAPI (endpoints, validaciones, conexión con Firestore)
