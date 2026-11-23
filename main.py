from flask import Flask, render_template, request, redirect, url_for, abort
import math

app = Flask(__name__)

# Lista en memoria para almacenar temporalmente los resultados enviados por los formularios.
# Los registros se mantienen mientras la aplicación Flask esté en ejecución.
registros = []


def obtener_siguiente_id():
    """Entrega un identificador consecutivo para cada resultado almacenado."""
    if len(registros) == 0:
        return 1
    return registros[-1]["id"] + 1


def validar_numero(valor, minimo, maximo, nombre_campo):
    """Convierte un dato a número decimal y comprueba que esté dentro del rango."""
    try:
        numero = float(valor)
    except (TypeError, ValueError):
        raise ValueError("Debes ingresar un valor numérico válido para " + nombre_campo + ".")

    if not math.isfinite(numero):
        raise ValueError(nombre_campo + " debe ser un número finito.")

    if numero < minimo or numero > maximo:
        raise ValueError(nombre_campo + " debe estar entre " + str(minimo) + " y " + str(maximo) + ".")

    return numero


@app.route("/", methods=["GET"])
def index():
    """Muestra el menú principal de la aplicación."""
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    """Recibe tres notas y la asistencia, calcula el promedio y determina el estado."""
    if request.method == "POST":
        try:
            nota1 = validar_numero(request.form.get("nota1"), 10, 70, "Nota 1")
            nota2 = validar_numero(request.form.get("nota2"), 10, 70, "Nota 2")
            nota3 = validar_numero(request.form.get("nota3"), 10, 70, "Nota 3")
            asistencia = validar_numero(request.form.get("asistencia"), 0, 100, "Asistencia")

            promedio = (nota1 + nota2 + nota3) / 3

            # Ambas condiciones deben cumplirse para obtener el estado APROBADO.
            if promedio >= 40 and asistencia >= 75:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"

            registro = {
                "id": obtener_siguiente_id(),
                "tipo": "promedio",
                "nota1": nota1,
                "nota2": nota2,
                "nota3": nota3,
                "asistencia": asistencia,
                "promedio": promedio,
                "estado": estado
            }
            registros.append(registro)
            return redirect(url_for("resultado", registro_id=registro["id"]))

        except ValueError as error:
            return render_template("ejercicio1.html", error=str(error), datos=request.form), 400

    return render_template("ejercicio1.html", error=None, datos={})


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    """Recibe tres nombres y determina cuál contiene más caracteres."""
    if request.method == "POST":
        nombre1 = request.form.get("nombre1", "").strip()
        nombre2 = request.form.get("nombre2", "").strip()
        nombre3 = request.form.get("nombre3", "").strip()
        nombres = [nombre1, nombre2, nombre3]

        if any(nombre == "" for nombre in nombres):
            return render_template(
                "ejercicio2.html",
                error="Debes completar los tres nombres.",
                datos=request.form
            ), 400

        # Se comprueba que los tres nombres sean distintos, sin distinguir mayúsculas.
        if len(set(nombre.casefold() for nombre in nombres)) != 3:
            return render_template(
                "ejercicio2.html",
                error="Debes ingresar tres nombres diferentes.",
                datos=request.form
            ), 400

        cantidades = [len(nombre) for nombre in nombres]
        mayor_cantidad = max(cantidades)
        nombres_mayores = [nombres[i] for i in range(3) if cantidades[i] == mayor_cantidad]

        registro = {
            "id": obtener_siguiente_id(),
            "tipo": "nombres",
            "nombres": nombres,
            "nombres_mayores": nombres_mayores,
            "cantidad_caracteres": mayor_cantidad
        }
        registros.append(registro)
        return redirect(url_for("resultado", registro_id=registro["id"]))

    return render_template("ejercicio2.html", error=None, datos={})


@app.route("/resultado/<int:registro_id>", methods=["GET"])
def resultado(registro_id):
    """Busca y muestra un resultado previamente almacenado en la lista en memoria."""
    for registro in registros:
        if registro["id"] == registro_id:
            return render_template("resultado.html", registro=registro)

    # Si el identificador no existe, se responde con un error HTTP 404.
    abort(404)


@app.errorhandler(404)
def pagina_no_encontrada(error):
    """Muestra una página de error cuando la ruta o el resultado no existe."""
    return render_template("resultado.html", registro=None, error_404=True), 404


if __name__ == "__main__":
    # El modo debug se utiliza únicamente durante el desarrollo y las pruebas locales.
    app.run(debug=True)
