from flask import Flask, render_template, request
import logic
import scraper

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    res = None
    if request.method == 'POST':
        try:
            monto_usd = float(request.form.get('monto_usd', 0))
            dolar_dia = scraper.obtener_dolar_dia()
            
            desc_usd = logic.calcular_descuento_usd(monto_usd)
            monto_neto_usd = monto_usd - desc_usd
            
            neto_clp = logic.convertir_usd_a_clp(monto_neto_usd, dolar_dia)
            iva = logic.calcular_iva_clp(neto_clp)
            total = logic.calcular_total_final(neto_clp, iva)
            
            res = {
                "valor_dolar": dolar_dia, "venta_usd": monto_usd,
                "descuento_usd": desc_usd, "neto_clp": neto_clp,
                "iva": iva, "total": total
            }
        except Exception as e:
            print(f"Error: {e}")
    return render_template('index.html', res=res)

if __name__ == '__main__':
    app.run(debug=True)
    