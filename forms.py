from wtforms import Form
from wtforms import StringField, TextAreaField,SelectField,RadioField
from wtforms import EmailField
from wtforms import validators

class numeros(Form):
    num1=StringField("Punto 1")
    num2=StringField("Punto 2")
    num3=StringField("Punto 3")
    num4=StringField("Punto 4")

class number(Form):
    num1=SelectField("Banda 1",choices=[('', 'SELECCIONA'),('', 'NEGRO'), ('1', 'CAFÉ'), ('2', 'ROJO'), ('3', 'NARANJA'), ('4', 'AMARILLO'), ('5', 'VERDE'), ('6', 'AZUL'), ('7', 'VIOLETA'), ('8', 'GRIS'), ('9', 'BLANCO')])
    num2=SelectField("Banda 2",choices=[('', 'SELECCIONA'),('', 'NEGRO'), ('1', 'CAFÉ'), ('2', 'ROJO'), ('3', 'NARANJA'), ('4', 'AMARILLO'), ('5', 'VERDE'), ('6', 'AZUL'), ('7', 'VIOLETA'), ('8', 'GRIS'), ('9', 'BLANCO')])
    num3=SelectField("Banda 3",choices=[('', 'SELECCIONA'),('', 'NEGRO'), ('0', 'CAFÉ'), ('00', 'ROJO'), ('000', 'NARANJA'), ('0000', 'AMARILLO'), ('00000', 'VERDE'), ('000000', 'AZUL'), ('0000000', 'VIOLETA'), ('00000000', 'GRIS'), ('000000000', 'BLANCO')])
    num4=RadioField('Banda 4 (Tolerancia)',choices=[('.05','Dorada:5%'),('.1','Plateada:10%')])


class Traductor(Form):
    palabra1 = StringField("Palabra en inglés", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=10, message='Ingrese una palabra válida')
    ])
    palabra2 = StringField("Palabra en Español", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=10, message='Ingrese una palabra válida')
    ])
    
class Busqueda(Form):   
    
    palabra = StringField("BUSCAR EN LISTA" ,[
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=10, message='Ingrese una palabra válida')
    ])
    num4=RadioField('Idioma',choices=[('1','Español'),('0','Ingles')])

