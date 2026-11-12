# CRUD de estudiantes

Aplicación web sencilla para registrar, consultar, actualizar y eliminar
estudiantes. Está construida con Flask y utiliza MySQL como base de datos.

## Requisitos

- Python 3
- Flask
- MySQL Connector/Python
- MySQL o XAMPP

## Instalación

Desde la carpeta del proyecto, crea y activa un entorno virtual:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Instala las dependencias:

```powershell
pip install Flask mysql-connector-python
```

## Base de datos

Crea la base de datos `institucion` y la tabla `estudiantes` en MySQL:

```sql
CREATE DATABASE institucion;
USE institucion;

CREATE TABLE estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo VARCHAR(150) NOT NULL,
    programa VARCHAR(150) NOT NULL
);
```

La aplicación está configurada para conectarse a MySQL en `127.0.0.1` con
el usuario `root` y la contraseña `usbw`. Ajusta estos valores en `app.py` si
tu instalación utiliza una configuración diferente.

## Ejecución

```powershell
python app.py
```

Abre <http://127.0.0.1:5000> en el navegador.
