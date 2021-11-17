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
from fpdf import FPDF
import smtplib # Correo
import datetime
from claseCliente import *
import re, names
from random import randint

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
    return list(pdict.keys())
    
def conseguirCantones(pdcit, pprovincia):
    """
    Función: Consigue los cantones de la provincia indicada
    Entradas: 
    -pdict(dict): Es el diccionario a sacar provincias
    -pprovincia(str): Es el nombre de la provincia a buscar 
    Salidas: Lista de los cantones de la provincia indicada
    """
    return list(pdcit[pprovincia].keys())

def conseguirDistritos(pdict, pprovincia, pcanton):
    """
    Función: Consigue el nombre de los distritos de un canton indicado
    Entradas:
    -pdict(dict): Es el diccionario a sacar provincias
    -pprovincia(str): Es el nombre de la provincia a buscar 
    -pcanton(str): es le canton a sacar distritos
    Salidas: Lista de los distritos del canton indicado
    """
    return list(pdict[pprovincia][pcanton].keys())

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

def validarCedula(pcedula):
    """
    Funcionalidad: Valida que se ingrese una cedula formato correcto
    Entradas: nombre(str): Nombre a validar 
    Salidas: Booleano 
    """
    if re.match('^[1-9]{1}\d{4}0{1}\d{3}$', pcedula):
        return pcedula
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

def crearCedula():
    """
    Función: Crea cédulas con el formato correcto de manera aleatoria
    Entradas: N/A
    Salidas: Str(); es la cédula
    """
    return f"{randint(1,9)}-{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}-{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"

def generarNombre(): 
    """
    Función:    Genera nombre y apellidos aleatorios para una persona.
    Entrada:    N/A 
    Salida:     String, nombre y apellidos aleatorios.
    """
    return (names.get_first_name(), names.get_last_name(), names.get_last_name())

def generarDirEspecifica():
    """
    Función: Se encarga de generar la dirección específica de un cliente
    Entradas: N/A
    Salidas: Str(); es la direccion especifica del cliente
    """
    return f"CA{randint(1, 60)} AV{randint(1, 60)} #{randint(1, 60)}"

def generarCodPostal_DirGeneral(pdictBD, pcedula):
    """
    Función: Crea el código postal de un cliente y su direccion general
    Entradas:
    -pdictBD(dict): Es el diccionario que contiene los datos de los codigos de distrito
    -pcedula(str): es la cedula del usuario para crear el codigo postal
    Salidas: Tuple(); en la primer posicion da el código postal, y en la segunda posicion da la direccion general
    """
    pcedula = pcedula[0]
    if not re.match("^[1-7]", pcedula):
        pcedula = "1" 
    provinciaIndicada = conseguirProvincias(pdictBD)[int(pcedula)-1]
    cantones = conseguirCantones(pdictBD, provinciaIndicada)
    cantonRandom = cantones[randint(0, len(cantones)-1)]
    distritos = conseguirDistritos(pdictBD, provinciaIndicada, cantonRandom)
    distritoRandom = distritos[randint(0, len(distritos)-1)]
    return (conseguirCodigo(pdictBD, provinciaIndicada, cantonRandom, distritoRandom), [provinciaIndicada, cantonRandom, distritoRandom])

def generarCorreo(ptupla, pflag=True):
    """
    Función: Genera el correo de un cliente 
    Entradas:
    -ptupla(tuple): es la tupla que contiene el nombre del cliente
    Salidas:
    """
    if pflag:
        return f"{ptupla[0][1]}{ptupla[1]}@gmail.com".lower()
    return f"{ptupla[0][1]}{ptupla[2]}@gmail.com".lower()

def encontrarCorreo(pcorreo, plistaBD):
    """
    Función: Determina si un correo ya existe en la base de datos de clientes
    Entradas:
    -pcorreo(str): Es el correo a buscar
    -plistaBD(list): Es la lista que contiene a los objetos (clientes)
    Salidas: Bool
    """
    for objeto in plistaBD:
        if objeto.obtenerCorreo() == pcorreo:
            return True
    return False

def encontrarCedula(pcedula, plistaBD):
    """
    Función: Determina si una cédula ya existe en la base de datos de clientes
    Entradas:
    -pcedula(str): Es la cédula a buscar
    -plistaBD(list): Es la lista que contiene a los objetos (clientes)
    Salidas: Bool
    """
    for objeto in plistaBD:
        if objeto.obtenerCedula == pcedula:
            return True
    return False
####################################
#          Generar clientes        #
####################################
def crearClientes(pcantidad, plistaBD, pdiccCodigos):
    while pcantidad != 0:
        cedula = crearCedula()
        if not encontrarCedula(cedula, plistaBD):
            nombre = generarNombre()
            correo = generarCorreo(nombre, plistaBD)
            if encontrarCorreo(correo, plistaBD):
                correo = generarCorreo(nombre, False)
            codigoDireccion = generarCodPostal_DirGeneral(pdiccCodigos, cedula)
            clienteActu = Cliente()
            clienteActu.asignarCedula(cedula), clienteActu.asignarNombre(nombre), clienteActu.asignarDirEspecifica(generarDirEspecifica()),
            clienteActu.asignarDirGeneral(codigoDireccion[1]), clienteActu.asignarCodigoPostal(codigoDireccion[0]), clienteActu.asignarCorreo(correo)
            plistaBD.append(clienteActu)
            pcantidad -= 1
    return plistaBD

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

