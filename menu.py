############################
# Importación de librerias # 
############################
from generarArchivos import *
from tkinter import *
from tkinter.font import BOLD
from typing import Sized
from funciones import *
from archivos import *
from tkinter import messagebox, ttk

############################
#    Variables globales    # 
############################

dicBD = lambda: crearBDCodigos()
clientes = lambda: leerBinarioLista("ClientesBD")

############################
# Definición de Funciones  # 
############################

#   ------------------------------------------------- Formato general  -------------------------------------------------
def crearBoton(pventana, ptexto, pfuncion):
    """
    Función:    Crea un botón con texto y comando para una ventana
    Entradas:
        pventana (tkinter.Tk)           - Ventana gráfica
        ptexto (str)                    - Texto del botón
        pfuncion (function)             - Acción del botón
        pwidth (str, opcional)          - Longitud del botón
        pgrid, pspan (tuple, opcional)  - Indican como acomodar botones
    Salidas:    Retorna el botón creado
    """
    boton = ttk.Button(pventana, text= ptexto, command= pfuncion)
    boton.config(width = "25")
    boton.pack(padx=30, pady=10)    # Acomoda botón creado
    return boton

def crearLabel(pventana, ptexto,pfont='arial',psize=12,pbg='#f0f0f0',pfg='black'):
    """
    Función:    Crea etiqueta para descripciones adicionales
    Entradas:
        pventana (tk.Toplevel)  - Ventana gráfica
        ptexto (str)            - Texto que se muestra
        pgrid (tuple, opcional) - Indica como acomodar texto y entrada
    Salidas:    Retorna el objeto (etiqueta) creado
    """
    etiqueta = tk.Label(pventana, text = ptexto)
    etiqueta.config(font=(pfont,psize),bg=pbg,fg=pfg)
    return etiqueta

def crearEntradaTexto(pventana, ptexto, pvariable, pjustify,pfont='arial',psize=12,pbg='#f0f0f0',pfg='black'):
    """
    Función:    Crea etiquetas y cajas de texto para una entrada
    Entradas:
        pventana (tk.Toplevel)           - Ventana gráfica
        ptexto, pjustify (str)           - Texto de entrada y como justificarlo
        pvariable (tk.StrVar/tk.IntVar)  - Variable donde se almacena entrada
        pgrid (tuple)                    - Indica como acomodar texto y entrada
    Salidas:    Retorna el objeto (entrada de texto) creado
    """
    # Objetos: etiqueta y boton
    texto = tk.Label(pventana, text= ptexto)
    texto.config(font=(pfont,psize),bg=pbg,fg=pfg)
    texto.pack()
    entrada = ttk.Entry(pventana, textvariable= pvariable, justify = pjustify)
    entrada.pack()
    return entrada

def crearCaja(pventana, ptexto, pvariable, pvalores, pjustify):
    """
    Función:    Crea caja de selección para entradas
    Entradas:
        pventana (tk.Toplevel)          - Ventana gráfica
        ptexto, pjustify (str)          - Texto de selección y como justificarlo
        pvariable (tk.StrVar/tk.IntVar) - Variable donde se almacena entrada
        pvalores (tuple)         - Valores disponibles 
    Salidas:    Retorna el objeto (caja de selección) creado
    """
    # Objetos: etiqueta, caja de selección
    texto = tk.Label(pventana, text= ptexto)
    select = ttk.Combobox(pventana, textvariable=pvariable, values=pvalores, state="readonly", justify=pjustify)
    # Posicionamiento grid
    texto.pack(padx=20, pady=10)
    select.pack(padx=30, pady=10)
    return select

def crearVentana(titulo):
    """
    Funcionalidad: Formato general para crear una nueva ventana 
    Entradas: titulo: Nombre de la ventana 
    Salidas: Ventana en la interfaz 
    """
    ventana = Tk()
    ventana.title(titulo)
    ventana.resizable(False,False)
    ventana.config(bg = '#f0f0f0')
    ventana.iconbitmap('icon.ico')
    ventana.update()
    return ventana

def dimensionarVentana(ventana, anchoVentana, altoVentana):
    """
    Funcionalidad: Ajusta el tamaño de la ventana según las medidas dadas
    Entradas: 
    -ventana: La ventana que se quiere dimensionar 
    -anchoVentana: El ancho que va a poseer la ventana 
    -altoVentana: El alto que va a poseer la ventana
    Salidas: Na 
    """
    anchoPantalla = ventana.winfo_screenwidth() # Toma el ancho de la pantalla de la computadora 
    altoPantalla = ventana.winfo_screenheight() # Toma el alto de la pantalla de la computadora
    posicionVentanaX = (anchoPantalla/2) - (anchoVentana/2) # Al dividir y restar, está ajustando la ventana al centro en eje X
    posicionVentanaY = (altoPantalla/2) - (altoVentana/2) # Al dividir y restar, está ajustando la ventana al centro en eje Y
    ventana.geometry('%dx%d+%d+%d' % (anchoVentana,altoVentana,posicionVentanaX,posicionVentanaY))

def mostrarError(pventana, pmensaje):
    """
    Función:    Despliega interfaz con mensaje de error
    Entradas:
        pventana (tkinter.Tk)   - Ventana de origen del mensaje
        pmensaje (str)          - Mensaje de error a mostrar
    Salidas:    Retorna objeto (dialogo de error)
    """
    return messagebox.showerror(title="Error", message = pmensaje, parent = pventana)

def mostrarInfo(pventana, pmensaje):
    """
    Función:    Despliega interfaz con información para usuario
    Entradas:
        pventana (tkinter.Tk)   - Ventana de origen del mensaje
        pmensaje (str)          - Mensaje de error a mostrar
    Salidas:    Retorna objeto (dialogo de información)
    """
    return messagebox.showinfo(title="Atención", message=pmensaje, parent=pventana)

def confirmarTk(pventana, pmensaje):
    """
    Función:    Despliega interfaz con pregunta a usuario
    Entradas:
        pventana (tkinter.Tk)   - Ventana de origen del mensaje
        pmensaje (str)          - Mensaje de pregunta a mostrar
    Salidas:    Retorna True si se acepta, False si se cancela
    """
    return messagebox.askokcancel(title="Atención", message=pmensaje, parent=pventana)

#   -------------------------------------------- VENTANA CARGAR CODIGOS -------------------------------------------------
def abrirVentanaCargarCodigos(pventana):
    """
    Funcionalidad: Al presionar el botón de extraer frases se abre esta abre una ventana que muestra un mensaje
    Entradas: Na 
    Salidas: Na
    """
    codigosPostalesDinamico = crearBDCodigos()
    if codigosPostalesDinamico == False:
        return mostrarError(pventana, "Error\nNo se ha encontrado el archivo que contiene los códigos postales.\nEl archivo se debe llamar: BDPostalCR.txt.")
    return mostrarInfo(pventana, "Se han cargado los códigos exitosamente.")

#   ----------------------------------------- VENTANA CREAR CLIENTES -------------------------------------------------
def esEntero(cantidadGrupos):
    """
    Funcionamiento: Permite ingresar la cantidad de grupos y la cantidad de estudiantes por grupo
    en la ventana de insertar n grupos 
    Entrada: 
    -cantidadGrupos(str): Cantidad de grupos a ingresar 
    -cantidadEstudiantesGrupos(str): Cantidad de estudiantes de cada grupo
    Salida: Lista de listas  
    """
    try: 
        return int(cantidadGrupos)
    except: 
        return None

def validarRegistrarClientes(pventana, pnum):
    listaClientes, dicCodigos, pnum = clientes(), dicBD(), esEntero(pnum)
    if pnum == None:
        return mostrarError(pventana, "Solo se deben ingresar números enteros.")
    elif pnum == 0:
        return mostrarError(pventana, "Se debe ingresar un número mayor a 0.")
    grabarBinario("ClientesBD", crearClientes(pnum, listaClientes, dicCodigos))
    return mostrarInfo(pventana, "Base de datos creada.")

def entradasRegistrarClientes(pventana):
    cantidadClientes = crearEntradaTexto(pventana, "Cantidad de clientes: ", tk.IntVar(), "center")
    funcion = lambda: validarRegistrarClientes(pventana, cantidadClientes.get())
    botonIngresar = crearBoton(pventana, "Crear", funcion)

def menuRegistrarClientes(pprincipal):
    """
    Funcionalidad: Al presionar el botón de insertar n grupos en la ventana principal, se abre o crea otra ventana 
    que me permite ingresar la información requerida
    Entradas: Na 
    Salidas: Na 
    """
    ventana = tk.Toplevel(pprincipal)
    # Configuracion de la ventana secundaria
    ventana.title("Crear clientes")
    ventana.geometry("300x170")
    ventana.resizable(0,0)
    ventana.iconbitmap('icon.ico')
    ventana.lift(pprincipal)    # Posiciona por encima de ventana principal
    dimensionarVentana(ventana, 350, 100)
    entradasRegistrarClientes(ventana)
###########################################   exportar   ##################################################
def exportarXML():
    dicCodigos = dicBD()
    crearXML(dicCodigos)
    return ""
########################################### Reportes     ##################################################   
###########################
# Reporte según provincia #
###########################
def validarReporteProvincia(pventana, pprovincia, pprovinciasTotales):
    listaClientes = clientes()
    if pprovincia == -1:
        return mostrarError(pventana, "Por favor escoja una provincia")
    return crearReporteProvincia(pprovinciasTotales[pprovincia], listaClientes)

def entradasReporteProvincia(pventana):
    BDCodigos = dicBD()
    provincias = conseguirProvincias(BDCodigos)
    cajaProv = crearCaja(pventana, "Escoja una provincia", tk.StringVar(), provincias, "center")
    cajaProv.set("- Provincias -")
    funcion = lambda: validarReporteProvincia(pventana, cajaProv.current(), provincias)
    boton = crearBoton(pventana, "Crear reporte", funcion)
    
def ventanaReporteProvincia(pventana):
    ventana = tk.Toplevel(pventana)
    # Configuracion de la ventana secundaria
    ventana.title("Reporte según provincia")
    ventana.geometry("490x300")
    ventana.resizable(0,0)
    ventana.lift(pventana)    # Posiciona por encima de ventana principal
    dimensionarVentana(ventana, 350, 200)
    entradasReporteProvincia(ventana)   # Crea y valida entradas
###########################
# Reporte según cédula    #
###########################
def validarReporteCedula(pventana, pcedula):
    listaClientes = clientes()
    pcedula = validarCedula(pcedula)
    if pcedula == False:
        return mostrarError(pventana, "El formato de cédula es incorrecto")
    elif not encontrarCedula(listaClientes):
        return mostrarInfo(pventana, "La cédula ingresada todavía no ha sido ingresada.")
    return crearReporteCliente(pcedula, listaClientes)

def entradasReporteCedula(pventana):
    cedula = crearEntradaTexto(pventana, "Ingrese la cédula", tk.StringVar(), "center")
    funcion = lambda: validarReporteCedula(pventana, cedula)
    boton = crearBoton(pventana, "Generar reporte", funcion)

def ventaReporteCedula(pventana):
    ventana = tk.Toplevel(pventana)
    ventana.title("Reporte según cédula")
    ventana.lift(pventana)
    dimensionarVentana(ventana, 350, 200)
    entradasReporteCedula(ventana)

###############################
# Reporte según código postal #
###############################
def validarReporteCodigo(pventana, pcodigo):
    
def entradasReporteCodigo(pventana):
    entrada = crearEntradaTexto(pventana, "Ingrese el carné", tk.StringVar(), "center")
    funcion = lambda: validarReporteCodigo(pventana, entrada.get())
    boton = crearBoton(pventana, "Generar reporte", funcion)

def ventanaReporteCodigo(pventana):
    ventana = tk.Toplevel(pventana)
    ventana.title("Reporte según código postal")
    ventana.lift(pventana)
    dimensionarVentana(ventana, 350, 300)
    entradasReporteCodigo(ventana)

########################################### CREDENCIALES ##################################################    
def abrirVentanaCredenciales(pprincipal):
    """
    Funcionalidad: Al presionar el botón de insertar n grupos en la ventana principal, se abre o crea otra ventana 
    que me permite ingresar la información requerida
    Entradas: Na 
    Salidas: Na 
    """
    ventana = tk.Toplevel(pprincipal)
    # Configuracion de la ventana secundaria
    ventana.title("Credenciales")
    ventana.geometry("400x170")
    ventana.resizable(0,0)
    ventana.config(bg='black')
    ventana.iconbitmap('icon.ico')
    ventana.lift(pprincipal)  # Posiciona por encima de ventana principal
    dimensionarVentana(ventana, 800, 500)
    imagenMario=PhotoImage(file='Mario.png')
    imagenCamilo=PhotoImage(file='camilo.png')
    labelMario = Label(ventana,image=imagenMario).place(x=50,y=50)
    labelCamilo=Label(ventana,image=imagenCamilo).place(x=500,y=50)
    label = crearLabel(ventana,'Developers','Franklin Gothic Medium',psize=20,pbg='black',pfg='white').place(x=320,y=5)
    labelC =  crearLabel(ventana,'Camilo Sánchez','Franklin Gothic Medium',psize=20).place(x=510,y=420)
    labelM = crearLabel(ventana,'Mario Barboza','Franklin Gothic Medium',psize=20).place(x=60,y=420)
    ventana.mainloop()
#   ------------------------------------------------- VENTANA PRINCIPAL -------------------------------------------------
def colocarBotonesVentanaPrincipal(ventanaPrincipal):
    """
    Funcionalidad: Coloca los botones en la ventana principal 
    Entradas: La ventana principal 
    Salidas: Na (interfaz)
    """
    nombresBotones = ("1. códigos postales.", "2. Registrar Cliente.", "3. Crear Clientes.", "4. Generar Etiqueta.",
    "5. Enviar Correo.", "6. Exportar Códigos.", "7. Reportes.", "8. Credenciales.", "9. Salir.")        
    funciones = (lambda: abrirVentanaCargarCodigos(ventanaPrincipal), lambda: abrirVentanaIngresarCliente(ventanaPrincipal), 
                lambda: menuRegistrarClientes(ventanaPrincipal), lambda: abrirVentanaPdfEtiqueta(ventanaPrincipal), 
                lambda: print("Enviar correo"), lambda: exportarXML(), 
                lambda: ventanaReporteProvincia(ventanaPrincipal), lambda: abrirVentanaCredenciales(ventanaPrincipal))
    botonCargarCodigos = crearBoton(ventanaPrincipal, nombresBotones[0], funciones[0])
    botonRegistraCliente = crearBoton(ventanaPrincipal, nombresBotones[1], funciones[1])
    botonInsertarClientes = crearBoton(ventanaPrincipal, nombresBotones[2], funciones[2])
    botonCrearEtiqueta = crearBoton(ventanaPrincipal, nombresBotones[3], funciones[3])
    botonEnviarCorreo =  crearBoton(ventanaPrincipal, nombresBotones[4], funciones[4])
    botonExportarCodigos = crearBoton(ventanaPrincipal, nombresBotones[5], funciones[5])
    botonCrearReportes = crearBoton(ventanaPrincipal, nombresBotones[6], funciones[6])
    botonCredenciales = crearBoton(ventanaPrincipal, nombresBotones[7], funciones[7])
    botonSalir = crearBoton(ventanaPrincipal, nombresBotones[-1], ventanaPrincipal.destroy)
    return botonCargarCodigos, botonRegistraCliente, botonInsertarClientes, botonCrearEtiqueta, botonEnviarCorreo, botonExportarCodigos, botonCrearReportes, botonCredenciales

def iniciarInterfaz():
    """
    Funcionalidad: Crea la ventana principal que contendrá los botones principales 
    Entradas: Na 
    Salidas: Na 
    """
    ventanaPrincipal = crearVentana("Correos Costa Rica")
    dimensionarVentana(ventanaPrincipal, 370, 520)
    colocarBotonesVentanaPrincipal(ventanaPrincipal)
    ventanaPrincipal.mainloop()
#iniciarInterfaz()

