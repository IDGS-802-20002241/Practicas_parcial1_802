from flask import Flask, request, render_template

app=Flask(__name__)

'''     
Decoradores o rutas
'''

@app.route("/formulario1",methods=["GET","POST"])
def calculo():
    resultado = None
    if request.method == "POST":
        num1 = int(request.form.get("n1"))
        num2 = int(request.form.get("n2"))
        operacion = request.form.get("operacion")

        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        elif operacion == "divicion":
            resultado = num1/num2
        else:
            resultado = "Operación no válida"

    return render_template("formulario1.html", resultado=resultado,n1=num1,n2=num2)
   
if __name__ == "__main__":
    app.run(debug=True)   
