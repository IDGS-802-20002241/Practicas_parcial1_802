from flask import Flask, request, render_template
import math
import forms
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
   

@app.route("/distancia",methods=["GET","POST"])
def distancia():
    resultado = None
    number_form=forms.number(request.form)
    if request.method == "POST":
        
        num1 = int(number_form.num1.data)
        num2 = int(number_form.num2.data)
      
        num3 = int(number_form.num3.data)
        num4 = int(number_form.num4.data)
      
        resultado= math.sqrt((num2 - num1)**2 + (num4 - num3)**2)
       
            
           

    return render_template("distancia.html", resultado=resultado, form = number_form)
   
if __name__ == "__main__":
    app.run(debug=True)   
