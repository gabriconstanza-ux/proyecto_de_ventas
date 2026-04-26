from flask import Flask, render_template, request
from services.calculator import calcular_total
from services.scraper import obtener_valor_dolar

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    error = None

    if request.method == "POST":
        try:
            monto = float(request.form["monto"])

            if monto < 0:
                raise ValueError("No se permiten valores negativos")

            dolar = obtener_valor_dolar()
            resultado = calcular_total(monto, dolar)
            resultado["dolar"] = dolar

        except Exception as e:
            error = str(e)

    return render_template("index.html", resultado=resultado, error=error)


if __name__ == "__main__":
    app.run(debug=True)

    
    