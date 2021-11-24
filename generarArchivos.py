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
from fpdf import FPDF

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
        Provincia = ET.SubElement(codigos, "Parte", provincia=provinciActu)
        for cantonActu in conseguirCantones(pdictCodigos, provinciActu):
            Canton = ET.SubElement(Provincia, "Parte", canton=cantonActu)
            for distritoActu in conseguirDistritos(pdictCodigos, provinciActu, cantonActu):
                Distrito = ET.SubElement(Canton, "Parte", distrito=distritoActu)
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
######################################### HTML ########################################################
def mostrarDirGeneral(plista):
    """
    Función: Muesta la dirección general de un cliente
    Entradas:
    -plista(list): Es la lista que contiene la direccion general
    Salidas: Str(); es la direccion general en formato para el usuario
    """
    return f"{plista[0]} > {plista[1]} > {plista[2]}"

def mostrarDirEspecifica(pstring):
    """
    Función: Muesta la dirección específica de un cliente
    Entradas:
    -pstring(str): Es el string que contiene la direccion especifica del cliente
    Salidas: Str(); es la direccion especifica, para mostrar en el HTML
    """
    pstring = pstring.split()
    return f"<b>CA</b>{pstring[0][2:]}<b> AV</b>{pstring[1][2:]} <b>#</b>{pstring[2][1:]}"

def crearNombreArch(pstring):
    """
    Función:    Genera string para nombrar archivos de salida
    Entradas:   pstring (str) - Nombre de archivo
    Salidas:    Retorna string de nombre con fecha y hora de creación
    """
    fecha = datetime.datetime.now() # Obtiene fecha y tiempo
    fecha = fecha.strftime("%d-%m-%Y-%H-%M-%S") # Formato a dd-mm-aaaa-hh-mm-ss
    return f"{pstring}-{fecha}"

def guardarArchHTML(pnomArch, pstring):
    """
    Funcionamiento: Se encarga de crear un archivo HTML
    Entradas:
    pnomArch(str): Es el nombre con el que se creará el archivo
    pstring(str): Es lo que se verá en el archivo html
    Salidas: Na 
    """
    pnomArch = f"{pnomArch}.html"
    fo = open(pnomArch, "w")
    fo.write(pstring)
    fo.close()
    os.startfile(pnomArch)
    return ""

def crearReporteProvincia(pprovincia, plistaObjetos):
    """
    Función: Crea reportes HTML según la provincia indicada
    Entradas:
    -pprovincia(str): Es la provincia a buscar
    -plistaObjetos(list): Lista de los clientes
    Salidas: N/A
    """
    tabla = f"""<html> 
    <head> <meta charset = "ISO 8859-1"/> <title> Reporte {pprovincia} </title> </head> <body> <table  width = "70%" border="2"> 
            <tr> <th colspan="6"> <div align ="center"><strong> Clientes de {pprovincia} </strong></div> </th> </tr> 
        <tr style=text-align:center> 
            <th> Cédula </th> <th> Nombre completo </th> <th> Dirección específica </th> <th> Dirección General </th> <th> Código postal </th>
        </tr>"""
    for cliente in plistaObjetos:
        dirGeneral = cliente.obtenerDirGeneral()
        if dirGeneral[0] == pprovincia:
            tabla += f"""<tr style=text-align:center> <td> {cliente.obtenerCedula()} </td>
            <td> {mostrarNombreCliente(cliente.obtenerNombre())} </td> <td> {mostrarDirEspecifica(cliente.obtenerDirEspecifica())} </td>
            <td> {mostrarDirGeneral(dirGeneral)} </td> <td> {cliente.obtenerCodigoPostal()} </td>"""
    guardarArchHTML(crearNombreArch(pprovincia), tabla+"</tr></table></body></html>")
    return ""

def crearReporteCliente(pcedula, plistaObjetos):
    """
    Función: Crea reporte según la cedula indicada
    Entradas:
    -pcedula(str): Es la cedula del cliente a buscar
    -plistaObjetos(list): es la lista donde se buscará la cedula
    Salidas: N/A
    """
    tabla = f"""<html> 
    <head> <meta charset = "ISO 8859-1"/> <title> Reporte {pcedula} </title> </head> <body> <table  width = "70%" border="2"> 
            <tr> <th colspan="6"> <div align ="center"><strong> Cédula del cliente: {pcedula} </strong></div> </th> </tr> 
        <tr style=text-align:center> 
            <th> Nombre completo </th> <th> Dirección específica </th> <th> Dirección General </th> <th> Código postal </th>
        </tr>"""
    for cliente in plistaObjetos:
        if cliente.obtenerCedula() == pcedula:
            tabla += f"""<tr style=text-align:center> <td> {mostrarNombreCliente(cliente.obtenerNombre())} </td>
            <td> {mostrarDirEspecifica(cliente.obtenerDirEspecifica())} </td>
            <td> {mostrarDirGeneral(cliente.obtenerDirGeneral())} </td> <td> {cliente.obtenerCodigoPostal()} </td>"""
            guardarArchHTML(crearNombreArch(pcedula), tabla+"</tr></table></body></html>")
            return ""

def crearReporteCodPostal(pcodigo, plistaObjetos):
    """
    Función: Crea reportes HTML según el codigo postal indicado
    Entradas:
    -pcodigo(int): Es el código postal a buscar
    -plistaObjetos(list): Es la lista de objetos donde se buscara el código postal
    Salidas: N/A
    """
    tabla = f"""<html> 
    <head> <meta charset = "ISO 8859-1"/> <title> Reporte {pcodigo} </title> </head> <body> <table  width = "70%" border="2"> 
            <tr> <th colspan="6"> <div align ="center"><strong> Reporte de clientes con el código: {pcodigo} </strong></div> </th> </tr> 
        <tr style=text-align:center> 
            <th> Cédula </th> <th> Nombre completo </th> <th> Dirección específica </th> <th> Dirección General </th> <th> Código postal </th>
        </tr>"""
    for cliente in plistaObjetos:
        codPostal = cliente.obtenerCodigoPostal()
        if codPostal == pcodigo:
            tabla += f"""<tr style=text-align:center> <td> {cliente.obtenerCedula()} </td>
            <td> {mostrarNombreCliente(cliente.obtenerNombre())} </td> <td> {mostrarDirEspecifica(cliente.obtenerDirEspecifica())} </td>
            <td> {mostrarDirGeneral(cliente.obtenerDirGeneral())} </td> <td> {codPostal} </td>"""
    guardarArchHTML(crearNombreArch(pcodigo), tabla+"</tr></table></body></html>")
    return ""
"""
bd = crearBDCodigos()
crearXML(bd)
x = crearClientes(400, [], bd)
for cliente in x:
    cliente.mostrarDatos()
crearReporteProvincia("San José", x)
a = input("Ingresa una cedula, breve: ")
crearReporteCliente(a, x)
a = input("Ingresa un codigo postal: ")
crearReporteCodPostal(a, x)
"""