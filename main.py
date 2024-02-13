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
    operacion = request.form.get("operacion")
    if request.method == "POST":
        
        num1 = int(number_form.num1.data)
        num2 = int(number_form.num2.data)
      
        num3 = int(number_form.num3.data)
        num4 = request.form.get("operacion")
      
        resultado= math.sqrt((num2 - num1)**2 + (num4 - num3)**2)
       
            
           

    return render_template("distancia.html", resultado=resultado, form = number_form)

@app.route("/resistencias", methods=["GET", "POST"])
def resistencia():
    resultado = ''
    resultado2 = 0.0 
    resultado3 = 0.0 
    num1 = 0  # Valor inicial
    num2 = 0  # Valor inicial
    num3 = 0  # Valor inicial
    num4 = 0.0  # Valor inicial

    number_form = forms.number(request.form)
    
    if request.method == "POST":
        num1 = number_form.num1.data
        num2 = number_form.num2.data
        num3 = number_form.num3.data
        num4 = float(number_form.num4.data)
      
        resultado = str(num1) + str(num2)+str(num3)
        resultado2 = float(resultado) - (float(resultado) * num4)
        resultado3 = float(resultado) + (float(resultado) * num4)

    return render_template("resistencia.html", resultado= resultado, resultado2=resultado2, resultado3=resultado3,
                           form=number_form, color=obtener_color(str(num1)), color2=obtener_color(str(num2)),
                           color3=obtener_color(str(num3)), color4=obtener_color(num4))

def obtener_color(num):
    if num == '':
        return 'black'
    elif num == .05:
        return 'gold'
    elif num == .1:
        return 'silver'
    elif num == '1' or num == '0':
        return 'brown'
    elif num == '2' or num == '00':
        return 'red'
    elif num == '3' or num == '000':
        return 'orange'
    elif num == '4' or num == '0000':
        return 'yellow'
    elif num == '5' or num == '00000':
        return 'green'
    elif num == '6' or num == '000000':
        return 'blue'
    elif num == '7' or num == '0000000':
        return 'violet'
    elif num == '8' or num == '00000000':
        return 'gray'
    else:
        return 'white'


   
if __name__ == "__main__":
    app.run(debug=True)   
