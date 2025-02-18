# Structure

```plaintext
/backend
│── /app
│   ├── /api                # Routers de la API (endpoints)
│   │   ├── /v1             # Versionado de API (opcional)
│   │   │   ├── __init__.py
│   │   │   ├── endpoints.py  # Archivo con las rutas principales
│   │   │   ├── auth.py       # Endpoints relacionados con autenticación
│   │   │   ├── chat.py       # Endpoints relacionados con OpenAI/LLM
│   │   │   ├── users.py      # Endpoints relacionados con usuarios
│   │   │   ├── tasks.py      # Otros endpoints específicos del negocio
│   │   │   ├── utils.py      # Funciones auxiliares específicas de la API
│   │
│   ├── /core               # Configuración central de la app
│   │   ├── __init__.py
│   │   ├── config.py       # Configuración general y variables de entorno
│   │   ├── security.py     # Seguridad y autenticación
│   │
│   ├── /models             # Modelos de la base de datos (SQLAlchemy/Pydantic)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── chat.py
│   │   ├── task.py
│   │
│   ├── /schemas            # Esquemas Pydantic para validación de datos
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── chat.py
│   │   ├── task.py
│   │
│   ├── /services           # Lógica de negocio e integración con OpenAI/LLM
│   │   ├── __init__.py
│   │   ├── openai_service.py  # Interacción con OpenAI API
│   │   ├── llm_service.py     # Capa de abstracción para modelos LLM
│   │   ├── user_service.py    # Funciones relacionadas con usuarios
│   │   ├── task_service.py    # Funciones relacionadas con tareas
│   │
│   ├── /db                 # Configuración de base de datos
│   │   ├── __init__.py
│   │   ├── session.py      # Creación de sesiones con SQLAlchemy
│   │   ├── models.py       # Importación de modelos
│   │   ├── crud.py         # Funciones CRUD genéricas
│   │
│   ├── /tests              # Pruebas unitarias y de integración (pytest)
│   │   ├── __init__.py
│   │   ├── test_users.py
│   │   ├── test_chat.py
│   │   ├── test_tasks.py
│   │
│   ├── main.py             # Punto de entrada de la aplicación FastAPI
│
├── .env                    # Variables de entorno
├── .gitignore              # Archivos a ignorar por Git
├── requirements.txt        # Dependencias del proyecto
├── docker-compose.yml      # Configuración de Docker (si usas contenedores)
├── Dockerfile              # Archivo para construir la imagen Docker (opcional)
├── README.md               # Documentación del proyecto
```
