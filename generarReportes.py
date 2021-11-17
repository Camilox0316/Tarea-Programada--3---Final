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

import xml.etree.cElementTree as ET
from funciones import *

##############################################################
#####              Definición de Funciones               #####
##############################################################
def guardarArchXML(parchivoNom, pBaseDatos):
    """
    Funcionamiento: Crear un arcivo con extension html
    Entradas:
    -parchivoNom(str): Es el nombre con el que se guardará el archivo
    -pBaseDatos(str): Es la informacion a escribir en el archivo
    Salidas: Na
    """
    fo = open(f"{parchivoNom}.xml", "w")
    fo.write(pBaseDatos)
    fo.close()
    return ""

def crearXML(pdictCodigos):
    """
    Función: Se encarga de exportar a formato XML el archivo de texto que provee los códigos postales
    Entradas: 
    -pdictCodigos(dict): Es el diccionario que contiene los códigos postales
    Salidas: N/A
    """
    codigos = ET.Element("Codigos")
    for provinciActu in conseguirProvincias(pdictCodigos):
        Provincia = ET.SubElement(codigos, "Provincia", provincia=provinciActu)
        for cantonActu in conseguirCantones(pdictCodigos, provinciActu):
            Canton = ET.SubElement(Provincia, "Canton", canton=cantonActu)
            for distritoActu in conseguirDistritos(pdictCodigos, provinciActu, cantonActu):
                Distrito = ET.SubElement(Canton, "Distrito", distrito=distritoActu)
                Codigo = ET.SubElement(Distrito, "Codigo").text=f"{conseguirCodigo(pdictCodigos, provinciActu, cantonActu, distritoActu)}"
    archivo = ET.tostring(codigos, encoding="utf8", method="xml").decode()
    guardarArchXML("codigoPostal", archivo)
    return ""
