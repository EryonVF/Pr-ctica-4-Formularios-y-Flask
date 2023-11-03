from flask import Flask, render_template

app = Flask(__name__)

# Ruta para la página principal
@app.route("/")
def index():
    return render_template("public/index.html")

# Rutas para las páginas adicionales
@app.route("/ruta1")
def ruta1():
    return render_template("public/ruta1.html")

@app.route("/ruta2")
def ruta2():
    return render_template("public/ruta2.html")

@app.route("/ruta3")
def ruta3():
    return render_template("public/ruta3.html")

if __name__ == "__main__":
    app.run()
