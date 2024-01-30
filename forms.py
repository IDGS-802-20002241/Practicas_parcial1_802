from wtforms import Form
from wtforms import StringField, TextAreaField,SelectField,RadioField
from wtforms import EmailField

class number(Form):
    num1=StringField("Punto 1")
    num2=StringField("Punto 2")
    num3=StringField("Punto 3")
    num4=StringField("Punto 4")

   