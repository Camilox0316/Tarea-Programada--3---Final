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
######################################### Etiquetas ########################################################
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