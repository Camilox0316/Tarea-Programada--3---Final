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

from archivos import *
import re

##############################################################
#####              Definición de Funciones               #####
##############################################################

############################################### Cargar Códigos ##################################################
def crearBDCodigos():
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
    return pdict.keys()
def conseguirCantones(pdcit, provincia):
    return pdcit[provincia].keys()
def conseguirDistritos(pdict, pcanton, pprovincia):
    return pdict[pprovincia][pcanton].keys()

def conseguirCodigo(pdict, pprovincia, pcanton, pdistrito):
    return pdict[pprovincia][pcanton][pdistrito]

def crearCodigosPostales():
    diccionario = pasarDiccionario()
    matriz = []
    for indice, llave in enumerate(diccionario.keys()):
        matriz.append([llave]) # [[san jose, []]]
        for canton, distrito in diccionario[llave].items():
            matriz[indice].append([canton, distrito]) 
    return matriz

BD = pasarDiccionario()
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
def validarNombre(nombre):
    """
    Funcionalidad: Valida que se ingrese un nombre, sin numeros ni caracteres
    Entradas: nombre(str): Nombre a validar 
    Salidas: Booleano 
    """
    if re.match('^[a-zA-Z]{1,}\s{1}[a-zA-Z]{1,}\s{1}[a-zA-Z]{1,}$',nombre):
        return True
    return False

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
