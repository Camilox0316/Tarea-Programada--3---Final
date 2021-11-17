"""
Elaborador por:       
- Mario Barboza Artavia
- Camilo Sánchez Rodríguez
Fecha de creación:    10/11/2021, 00:17
Última edición:       31/10/2021, 10:40 XM
Versión:              Python 3.9.6
"""
##############################################################
#####              Importación de Librerías              #####
##############################################################

from datetime import *
from pickle import *
from archivos import *
import re
from fpdf import FPDF
import smtplib # Correo
import datetime


##############################################################
#####              Definición de Funciones               #####
##############################################################
####################################
#         Lectura de códigos       #
####################################
def crearBDCodigos():
    """
    Función: mantiene en memoria los códigos de los distritos
    Entradas: N/A
    Salidas:
    -diccionario(dict): Contiene: {Provincia: {Cantones: {Distritos: Código}}}
    """
    parchivo = leerTXT("BDPostalCR.txt").splitlines()
    diccionario = {}
    for elemento in parchivo:
        actual = elemento.split(";") # [provincia, canton, distrito, codigo]
        provincia, canton = actual[0], actual[1]
        if provincia not in diccionario.keys():
            diccionario[provincia] = {}
        if canton not in diccionario[provincia].keys():
            diccionario[provincia].update({canton: {}})  
        diccionario[provincia][canton].update({actual[-2]: actual[-1]})
    return diccionario

def conseguirProvincias(pdict):
    """
    Función: Consigue las provincias del archivo
    Entradas: 
    -pdict(dict): Es el diccionario a sacar provincias
    Salidas: La lista con las provincias
    """
    return pdict.keys()
    
def conseguirCantones(pdcit, pprovincia):
    """
    Función: Consigue los cantones de la provincia indicada
    Entradas: 
    -pdict(dict): Es el diccionario a sacar provincias
    -pprovincia(str): Es el nombre de la provincia a buscar 
    Salidas: Lista de los cantones de la provincia indicada
    """
    return pdcit[pprovincia].keys()

def conseguirDistritos(pdict, pprovincia, pcanton):
    """
    Función: Consigue el nombre de los distritos de un canton indicado
    Entradas:
    -pdict(dict): Es el diccionario a sacar provincias
    -pprovincia(str): Es el nombre de la provincia a buscar 
    -pcanton(str): es le canton a sacar distritos
    Salidas: Lista de los distritos del canton indicado
    """
    return pdict[pprovincia][pcanton].keys()

def conseguirCodigo(pdict, pprovincia, pcanton, pdistrito):
    """
    Función: Consigue el codigo postal de un distrito
    Entradas: 
    -pdict(dict): Es el diccionario a sacar provincias
    -pprovincia(str): Es el nombre de la provincia a buscar 
    -pcanton(str): es le canton a sacar distritos
    Salidas: Es el código del distrito
    """
    return pdict[pprovincia][pcanton][pdistrito]
####################################
#             Validaciones         #
####################################
def validarNombre(pnombre):
    """
    Función:    Determina si el valor ingresado coincide con el formato de nombre , no permite números
    Entradas:
        -pnombre(str):  Es el nombre a verificar si cumple con el formato
    Salidas:
        -Retorna None y False para formato y caractéres inválidos, pnombre si es válido
    """
    pnombre = tuple(pnombre.split())
    if not len(pnombre) == 3:
        return None
    for nombre in pnombre:
        if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚ]{3,}$", nombre):
            return False
    return pnombre

def validarFormatoCorreo(pcorreo):
    """
    Funcionamiento: valida que el correo ingresado tenga formato correcto, y que además el correo exista previamente
    Entradas:
    -pcorreo(str): es el correo a validar
    Salidas:
    """
    if re.match("^[a-z\d]+[\._]?[a-z\d]+[@]\w+[.]\w{2,}$", pcorreo):
        return pcorreo
    return False
####################################
#        Utilidades extras         #
####################################
def mostrarNombreCliente(ptupla):
    """
    Función: Da el nombre de un cliente a partir de su tupla
    Entradas: 
    -ptupla(tuple): Es la tupla que contiene el nombre del cliente
    Salidas: Str(); el nombre del usuario
    """
    return f"{ptupla[0]} {ptupla[1]} {ptupla[2]}"

def crearCodigosPostales():
    diccionario = crearBDCodigos()
    matriz = []
    for indice, llave in enumerate(diccionario.keys()):
        matriz.append([llave]) # [[san jose, []]]
        for canton, distrito in diccionario[llave].items():
            matriz[indice].append([canton, distrito]) 
    return matriz
"""
Se va a pedir el codigo de San José -> Santa Ana -> Piedades; el cual es: 10905
"""
#print(f'Y el código postal es: {conseguirCodigo(BD, "San José", "Santa Ana", "Piedades")}')
#print(conseguirProvincias(BD))
#print('--------------------------------------------------')
#print(conseguirCantones(BD,'Alajuela'))
# #print(list(conseguirCantones(BD,'Puntarenas')))
#print('--------------------------------------------------')
#print(conseguirDistritos(BD,'San Ramón','Alajuela'))


########################################### Validaciones ################################################
def validarCedula(cedula):
    """
    Funcionalidad: Valida que se ingrese una cedula formato correcto
    Entradas: nombre(str): Nombre a validar 
    Salidas: Booleano 
    """
    if re.match('^[1-9]{1}\d{4}0{1}\d{3}$',cedula):
        return True
    return False
def verificarArchivo(nombreArchivo): 
    """
    Funcionalidad: verifica si el archivo existe
    Entradas: nombre de archivo
    Salidas: Bool
    """
    return leerTXT(nombreArchivo) == ""
def verificarCedula(carnet): 
    """
    Funcionalidad: Verifica si hay una cedula repetida
    Entradas: carnet
    Salidas: booleano
    """
    lista = list(lee(""))#lee el archivo de las personas que esten registradas
    for elem in lista: 
        if carnet == elem[0]: 
            return True 
    return False 
def validarCodigoPostal(codigo):
    # crearFuncion que Haga una lista de Todos los códigos postales esta funcion tiene que validar
    # si existen códigos o no cumplen el formato
    lista = []
    return codigo in lista
    return matriz
def creaPdf(nombre,especifica,general,codigo):
    """
    Funcionalidad: Crea un Pdf de la etiqiueta 
    Entradas: Na
    Salidas: Reporte pdf  
    """
    class PDF(FPDF):
        def header(self):
            for elemento in (200,0,100):
                self.image('correo.png',elemento,-25,80)
            self.ln(60)
    pdf = PDF('L','mm','Letter')
    # Agregar Página
    pdf.add_page()
    pdf.add_font(family = 'serif', style = 'B', fname = 'fuentes/serif.ttf' , uni=True)
    pdf.add_font(family = 'serif2', style = '', fname = 'fuentes/serif2.ttf' , uni=True)
    pdf.set_font('serif','B',12)
    pdf.cell(220,10,nombre,ln=True,align='l',border='T,R,L')
    pdf.set_font('serif2','',12)
    pdf.cell(220,10,especifica,align='l',fill=0,border='R,L',ln=1)
    pdf.cell(220,10,general,align='l',fill=0,border='R,L',ln=2)
    pdf.cell(220,10,codigo,align='l',fill=0,border='R,L',ln=3)
    pdf.cell(220,10,'COSTA RICA',align='l',fill=0,border='R,L,B',ln=4)
    pdf.image('stamp.png',180,68,50,50)
    for elem in (200,100,0):
        pdf.image('correo.png',elem,150,80)
    pdf.output((f'{nombre}.pdf'))
    return 'Archivo Creado'
#creaPdf('Mario Barboza Artavia','Alajuela, San Ramon, San Ramón ','AV: 2 C: 2 #55 ' ,'1101010')

def enviarCorreo(correo,nombre):
    """
    Funcionalidad: Envia correo  
    Entradas: correo
    Salidas: NA  
    """
    tomorrow = str(datetime.date.today() + datetime.timedelta(days=1))
    message = f'Para informarle a {nombre}.\nLa entrega de su paquete es: {tomorrow}.'
    subject = 'Entrega de paquete'
    message = 'Subject: {}\n\n{}'.format(subject, message)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('correoscrmariocamilo@gmail.com','tareaProgramada')
    server.sendmail('correoscrmariocamilo@gmail.com',correo,message)
    server.quit()
    print('Correo enviado')
#enviarCorreo('marionetabar1@gmail.com','Mario')

