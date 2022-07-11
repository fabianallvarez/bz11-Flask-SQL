from . import app


@app.route("/")
def inicio():
    return "Pagina de inicio"

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    return "Crear movimiento"

@app.route("/modificar/<int:id>", methods=["GET", "POST"])
def actualizar(id):
    return f"Actualizar movimiento con ID={id}"

@app.route("/borrar/<int:id", methods=["GET", "POST"])
def eliminar(id):
    return f"Eliminar movimiento{id}"
