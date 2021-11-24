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

import pickle

##############################################################
#####              Definición de Funciones               #####
##############################################################
def guardarTXT(filePath, stringToWrite):
    """
    Función: Guarda un archivo con extensión .txt
    Entradas:
    -filePatch(str): Es el nombre del archivo 
    -stringToWrite(str): Es la informacion a aguardar en el archivo
    Salidas: N/A
    """
    fo = open(filePath, "w")   #crea el file si no existe
    fo.write (str(stringToWrite))
    fo.close()
    return ""

def leerTXT(filePath):
    """
    Función: Carga la información que haya en un archivo txt
    Entradas:
    -filePath(str): Es el nombre del archivo
    Salidas: Lo que se encuentre en el archivo
    """
    try:
        fo = open (filePath, 'r',  encoding="utf8")
        resultado = fo.read()
        fo.close()
        return resultado
    except:
        return ""
        
def leerBinarioLista(nomArchLeer):
    """
    F: lee archivo
    E: str nombrede archivo
    S: retorna la lista
    """
    try:
        f=open(nomArchLeer,"rb")
        lista = pickle.load(f)
        f.close()
        return lista
    except:
        return []

def grabarBinario(nomArchGrabar,lista):
    """
    F: crea archivo
    E: str y lo que desee añadir a lista
    S: N/A
    """
    try:
        f = open(nomArchGrabar,"wb")
        pickle.dump(lista,f)
        f.close()
        return ""
    except:
        return ''