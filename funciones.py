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

##############################################################
#####              Definición de Funciones               #####
##############################################################
def pasarDiccionario():
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
print(f'Y el código postal es: {conseguirCodigo(BD, "San José", "Santa Ana", "Piedades")}')