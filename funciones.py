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