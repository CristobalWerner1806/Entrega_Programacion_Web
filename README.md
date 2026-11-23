# Evaluación 3 – Programación Web | IPLACEX

Aplicación web desarrollada con Python y Flask para resolver los dos ejercicios solicitados en la pauta de evaluación.

## Requerimientos

- Python 3.10 o superior.
- pip.

## Crear y activar el entorno virtual

### Windows (PowerShell)

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Si PowerShell bloquea la activación, utilizar la terminal CMD:

```cmd
py -m venv venv
venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Ejecutar la aplicación

```bash
python main.py
```

Abrir en el navegador: http://127.0.0.1:5000

## Funcionalidades

- Menú principal con acceso a ambos ejercicios.
- Ejercicio 1: recibe tres notas (10 a 70) y asistencia (0 a 100), calcula el promedio y determina APROBADO únicamente cuando el promedio es al menos 40 y la asistencia al menos 75%.
- Ejercicio 2: recibe tres nombres diferentes, identifica el o los nombres con mayor cantidad de caracteres y muestra el total.
- Los formularios envían datos mediante POST. Los resultados se consultan mediante una ruta GET con identificador.
- Los resultados se almacenan temporalmente en una lista de Python en memoria. Se eliminan al detener o reiniciar la aplicación.
- Se controlan datos fuera de rango, campos vacíos, nombres repetidos y resultados inexistentes.

## Estructura

```text
Entrega_Programacion_Web/
├── main.py
├── requirements.txt
├── README.md
├── GITHUB_LINK.txt
├── .gitignore
├── templates/
│   ├── index.html
│   ├── ejercicio1.html
│   ├── ejercicio2.html
│   └── resultado.html
├── static/
│   └── css/
│       └── estilos.css
├── tests/
│   └── test_app.py
└── EVIDENCIAS/
    └── README_EVIDENCIAS.txt
```

## Comprobaciones recomendadas

1. Probar el menú y abrir ambos formularios.
2. Ejercicio 1: probar un caso aprobado (60, 50, 70; asistencia 80) y un caso reprobado por asistencia (60, 60, 60; asistencia 70).
3. Probar límites de notas y asistencia, incluyendo un valor fuera de rango.
4. Ejercicio 2: probar nombres de distinta longitud y nombres repetidos.
5. Abrir una URL de resultado inexistente y comprobar la respuesta 404.

## Publicación en GitHub

Desde la carpeta del proyecto:

```bash
git init
git add .
git commit -m "Entrega evaluacion 3 Programacion Web"
git branch -M main
git remote add origin https://github.com/USUARIO/Programacion-Web-IPLACEX.git
git push -u origin main
```

Reemplazar `USUARIO` por el nombre de la cuenta y actualizar `GITHUB_LINK.txt` con la URL real. No subir la carpeta `venv`.

## Nota sobre el modo de depuración

`debug=True` está habilitado para las pruebas locales y el aprendizaje. No debe utilizarse en un servidor de producción.
