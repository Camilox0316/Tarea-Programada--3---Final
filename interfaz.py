############################
# Importación de librerias # 
############################
from pickle import POP
from tkinter import *
from tkinter.font import BOLD
from typing import Sized
from funciones import *
from archivos import *
from tkinter import messagebox, ttk

############################
#    Variables globales    # 
############################

dicBD = crearBDCodigos()
clientes = []

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

def crearVentanaSecundaria(pventana, titulo, pancho, palto): 

    ventanaSecundaria = Toplevel(pventana)
    ventanaSecundaria.title(titulo)
    ventanaSecundaria.resizable(False,False)
    ventanaSecundaria.config(bg = '#153a7a')
    ventanaSecundaria.iconbitmap('icon.ico')
    ventanaSecundaria = dimensionarVentana(ventanaSecundaria, pancho, palto)
    return ventanaSecundaria  

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
#   ------------------------------------------ VENTANA INSERTAR ClIENTE -------------------------------------------------
def validarRegistrarClientes(pventana, pnum):
    if not esEntero(pnum):
        return mostrarError(pventana, "Solo se deben ingresar números enteros.")
    crearClientes(int(pnum), [], dicBD)
    return mostrarInfo(pventana, "Base de datos creada.")

def entradasRegistrarClientes(pventana):
    cantidadClientes = crearEntradaTexto(pventana, "Cantidad de clientes: ", tk.IntVar(), "center")
    funcion = lambda: validarRegistrarClientes(pventana, cantidadClientes.get())
    botonIngresar = crearBoton(pventana, "Crear", funcion)

def abrirVentanaIngresarCliente(pventana):
    """
    Funcionalidad: Al presionar el botón de insertar estudiante se abre esta ventana, la cual contiene cajas de texto
    menú de selección para ingresar los datos.
    Entradas: Na 
    Salidas: Na 
    """
    ventanaInsertarCliente = tk.Toplevel(pventana)
  # Configuracion de la ventana secundaria
    ventanaInsertarCliente.title("Registrar Cliente")
    ventanaInsertarCliente.geometry("400x170")
    ventanaInsertarCliente.resizable(0,0)
    ventanaInsertarCliente.iconbitmap('icon.ico')
    ventanaInsertarCliente.lift(pventana)  # Posiciona por encima de ventana principal
    dimensionarVentana(ventanaInsertarCliente, 350, 600)
    colocarComponentesVentanaInsertarCliente(ventanaInsertarCliente)
    ventanaInsertarCliente.mainloop()

def actualizarCantonesMostrar(provincia, cajaSeleccionP,cantonSeleccionado):
    """
    Funcionalidad: Actualiza las frases en la caja de seleccion, para que se muestren las que corresponden
    a la categoría seleccionada.
    Entradas: CategoriaSeleccionada, cajaSeleccionFrases, fraseSeleccionada
    Salidas: Actualiza la variable con las frases de la categoría seleccionada 
    """
    print(provincia)
    cantones = conseguirCantones(dicBD,provincia)
    cantonesMostrados = []
    for cantoncito in cantones:
        cantonesMostrados.append(cantoncito)
    cajaSeleccionP["menu"].delete(0,"end")
    for canton in cantonesMostrados:
        cajaSeleccionP["menu"].add_command(label=canton, command=lambda canton=canton: cantonSeleccionado.set(canton))

def actualizarDistritosMostrar(provincia, canton, cajaSeleccionC,distritoSeleccionado):
    """
    Funcionalidad: Actualiza las frases en la caja de seleccion, para que se muestren las que corresponden
    a la categoría seleccionada.
    Entradas: CategoriaSeleccionada, cajaSeleccionFrases, fraseSeleccionada
    Salidas: Actualiza la variable con las frases de la categoría seleccionada 
    """
    print('hola')
    print(provincia)
    print(canton)
    if provincia == 'Seleccione una Provincia:' or canton == 'Seleccione un Cantón:':
        return cajaSeleccionC["menu"].add_command(label='', command=lambda distrito='': distritoSeleccionado.set(distrito))
    distritos = conseguirDistritos(dicBD,provincia,canton)
    print(distritos)
    distritosMostrados = []
    for distitrito in distritos:
        distritosMostrados.append(distitrito)
    cajaSeleccionC["menu"].delete(0,"end")
    for distrito in distritosMostrados:
        cajaSeleccionC["menu"].add_command(label=distrito, command=lambda distrito=distrito: distritoSeleccionado.set(distrito))
    return distrito
def colocarComponentesVentanaInsertarCliente(ventanaInsertarCliente):
    """
    Funcionalidad: Coloca los componentes(cajas de texto,labels, caja de seleccion) en la ventana
    de insertar estudiante.
    Entradas: La ventana en la que se van a unicar los componentes(VentanaInsertarEstudiante)
    Salidas: Na 
    """
    cedula = crearEntradaTexto(ventanaInsertarCliente, "Cédula: ", tk.StringVar(), "center",psize=10).pack(padx=20, pady=0)
    nombre = crearEntradaTexto(ventanaInsertarCliente, "Nombre: ", tk.StringVar(), "center",psize=10).pack(padx=20, pady=15)
    uEspecifica=crearEntradaTexto(ventanaInsertarCliente, "Ubicación Específica: ", tk.StringVar(), "center",psize=10).pack(padx=20, pady=15)
    uGeneral=crearEntradaTexto(ventanaInsertarCliente, "Ubicación General: ", tk.StringVar(), "center",psize=10).pack(padx=20, pady=0)
    #try:
    Provincias =  conseguirProvincias(dicBD)
    ProvinciaSeleccionada = StringVar(ventanaInsertarCliente) #StrVar declara una variable de tipo cadena
    ProvinciaSeleccionada.set("Seleccione una Provincia:")
    
    Cantones = [""]
    CantonSeleccionado = StringVar(ventanaInsertarCliente)
    CantonSeleccionado.set("Seleccione un Cantón:")
    
    Distritos = [""] 
    DistritoSeleccionado = StringVar(ventanaInsertarCliente)
    DistritoSeleccionado.set("Seleccione un Distrito: ")

    Codigo = [""]
    CodigoSeleccionado = StringVar(ventanaInsertarCliente)
    CodigoSeleccionado.set("Su código postal es:")

    cajaSeleccionCodigo = OptionMenu(ventanaInsertarCliente, CodigoSeleccionado, *Codigo)

    cajaSeleccionDistrito = OptionMenu(ventanaInsertarCliente, DistritoSeleccionado, *Distritos)

    cajaSeleccionCanton = OptionMenu(ventanaInsertarCliente, CantonSeleccionado, *Cantones,
    command=actualizarDistritosMostrar(ProvinciaSeleccionada.get(),CantonSeleccionado.get(),cajaSeleccionDistrito,
    DistritoSeleccionado))
    
    cajaSeleccionProvincia = OptionMenu(ventanaInsertarCliente, ProvinciaSeleccionada, *Provincias, 
    command=lambda ProvinciaSeleccionada: actualizarCantonesMostrar(ProvinciaSeleccionada, cajaSeleccionCanton, CantonSeleccionado))
    
    cajaSeleccionProvincia.pack(padx=20, pady=30)
    cajaSeleccionCanton.pack(padx=20, pady=0)
    cajaSeleccionDistrito.pack(padx=20, pady=30)
    cajaSeleccionCodigo.pack(padx=20, pady=0)

    botonInsertar=crearBoton(ventanaInsertarCliente,'Ingresar Cliente','')
    
    #except:
    #    mostrarError(ventanaInsertarCliente,'Error')

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
        cantidadGrupos = int(cantidadGrupos)
        # Meter una Función que cree base de datos y si ya existe que las una 
        return True 
    except:
        return False

def validarRegistrarClientes(pventana, pnum):
    if not esEntero(pnum):
        return mostrarError(pventana, "Solo se deben ingresar números enteros.")
    crearClientes(int(pnum), [], dicBD)
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
    
############################################## ETIQUIETA  ###############################################
def abrirVentanaPdfEtiqueta(pventana):
    """
    Funcionalidad: Genera una etiqueta
    Entradas: Na 
    Salidas: reporte pdf 
    """
    return ""
#   ------------------------------------------------- VENTANAS DE REPORTES  -------------------------------------------------
def colocarBotonesVentanaReportes(ventanaReportes):
    """
    Funcionalidad: Coloca los botones en la ventana de reportes 
    Entradas: VentanaReportes 
    Salidas:Na
    """
    reporteProvincias = crearBoton(ventanaReportes, "Reporte segun provincia", abrirVentanaReportesProvincia(ventanaReportes))
    reporteCliente = crearBoton(ventanaReportes, "Reporte según cliente", abrirVentanaReporteCliente())
    reporteCodigo = crearBoton(ventanaReportes, "Reporte según código", abrirVentanaReporteCodigos())

    botonRegresar = Button(ventanaReportes,text="Regresar")
    botonRegresar.config(width = "25",fg="black",font= ("Arial", 12),bg='white', command=ventanaReportes.destroy)
    botonRegresar.pack(padx=30, pady=10)

def abrirVentanaReportes(pventana):
    """
    Funcionalidad: Al presionar el botón de reportes en la ventana principal, se crea una ventana que contiene
    los botones para generar reportes según la especificación
    Entradas: Na
    Salidas: Na
    """ 
    ventanaReportes = tk.Toplevel(pventana)
    ventanaReportes.title("Reportes")
    ventanaReportes.resizable(0,0)
    ventanaReportes.lift(pventana)
    dimensionarVentana(ventanaReportes, 350, 100)
    colocarBotonesVentanaReportes(ventanaReportes)
    ventanaReportes.mainloop()

##########################################   Reporte 1   #############################################
def abrirVentanaReportesProvincia(pventana):
    """
    Funcionalidad: Crea una ventana que contiene una caja de seleccion de los grupos existentes 
    Entradas: Na 
    Salidas:Ventana 
    """
    try:
        Provincias =  conseguirProvincias(dicBD)
        ventanaReportesProvincia = crearVentanaSecundaria(pventana, "Reportes por Provincia", 350, 110)
        grupoSeleccionado = StringVar(ventanaReportesProvincia)
        grupoSeleccionado.set("Seleccione una Provincia")
        cajaSeleccionProvincia = OptionMenu(ventanaReportesProvincia, grupoSeleccionado, *Provincias)
        cajaSeleccionProvincia.pack(padx=20, pady=10)
        #cajaSeleccionGrupo.pack(padx=20, pady=10)
        botonGenerar = Button(ventanaReportesProvincia,text="Generar", command=lambda:generarReportePorClientesProvincia(grupoSeleccionado.get()))
        botonGenerar.config(width = "25",fg="black",font= ("Arial", 12))
        botonGenerar.pack(padx=30, pady=10)
        ventanaReportesProvincia.mainloop()
    except: 
         mostrarError(ventanaReportesProvincia,'Error')
def generarReportePorClientesProvincia(grupoSeleccionado):
    """
    Funcionalidad: Dado la provincia este genera el reporte HTML 
    Entradas: Provincia(str)
    Salidas: reporte html 
    """
    ventanaReportesProvincia = crearVentanaSecundaria(grupoSeleccionado, "Reporte Cliente", 350, 110)
    if grupoSeleccionado != "Seleccione una Provincia": # va a ser la provincia
        # Genera html de los clientes de una provincia 
        labelInforme = Label(ventanaReportesProvincia, text=f"Se ha creado el reporte de clientes {grupoSeleccionado} \ncon éxito.")
        labelInforme.pack(padx=20, pady=30)
        labelInforme.config(font=('Helvatical bold', 13), bg = '#153a7a')
    else: 
        labelInforme = Label(ventanaReportesProvincia, text="Debe seleccionar una Provincia.")
        labelInforme.pack(padx=20, pady=30)
        labelInforme.config(font=('Helvatical bold', 13), bg = '#153a7a')
##########################################   Reporte 2   #############################################
def abrirVentanaReporteCliente(pventana):
    """
    Funcionalidad: Crea una ventana con la caja de seleccion para que se ingrese la categoria 
    de la que se quiere hacer el reporte
    Entradas: Na
    Salidas: ventana 
    """
    ventanaReporteCliente = crearVentanaSecundaria(pventana, "Reportes por categoría de frase", 350, 110)
    entryCedula = Entry(ventanaReporteCliente, width=100, justify="center")
    entryCedula.config(font=('Helvatical bold', 10))
    entryCedula.pack(padx=30, pady=0)

    botonGenerar = Button(ventanaReporteCliente,text="Generar", command=lambda:generarReportePorCliente(entryCedula.get(),ventanaReporteCliente))
    botonGenerar.config(width = "25",fg="black",font= ("Arial", 12))
    botonGenerar.pack(padx=30, pady=10)
    ventanaReporteCliente.mainloop()
def generarReportePorCliente(cedulaSeleccionada,ventanaReporteCliente):
    """
    Funcionalidad: Dada la cedula se crea un html de cliente específico
    Entradas: categoria Seleccionada(str)
    Salidas: reporte html 
    """
    if validarCedula(cedulaSeleccionada):
        # Función que genere html de cliente especifico meterla en esta linea
        mostrarInfo(ventanaReporteCliente,f"Se ha creado el reporte de la persona:\n{cedulaSeleccionada}")#Promete función que pase de cedula a persona
    else: 
        mostrarError(ventanaReporteCliente,"Error, cédula con formato incorrecto.\nO no existente")
##########################################   Reporte 3    #############################################
def abrirVentanaReporteCodigos():
    """
    Funcionalidad: Crea una ventana 
    Entradas: Na
    Salidas: ventana 
    """
    ventanaReporteCodigo = crearVentanaSecundaria("Reportes por código", 350, 110)
    entryCodigo = Entry(ventanaReporteCodigo, width=100, justify="center")
    entryCodigo.config(font=('Helvatical bold', 10))
    entryCodigo.pack(padx=30, pady=0)

    botonGenerar = Button(ventanaReporteCodigo,text="Generar", command=lambda:generarReporteCodigos(entryCodigo.get(),ventanaReporteCodigo))
    botonGenerar.config(width = "25",fg="black",font= ("Arial", 12))
    botonGenerar.pack(padx=30, pady=10)
    ventanaReporteCodigo.mainloop()
def generarReporteCodigos(codigoSeleccionado,ventanaReporteCliente):
    """
    Funcionalidad: Dado el codigo postal se crea un html de clientes
    Entradas: Codigo Seleccionada(str)
    Salidas: reporte html 
    """
    if validarCodigoPostal(codigoSeleccionado):
        # Función que genere html de cliente especifico meterla en esta linea
        mostrarInfo(ventanaReporteCliente,f"Se ha creado el reporte del código:\n{codigoSeleccionado}")
    else: 
        mostrarError(ventanaReporteCliente,"Error, código con formato incorrecto.\nO código no existente")
        
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
                lambda: print("Agregar la funcion"), lambda: print("Agregar la funcion"), 
                lambda: abrirVentanaReportes(ventanaPrincipal), lambda: abrirVentanaCredenciales(ventanaPrincipal))
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

if __name__ == "__main__": #Si se ha ejecutado como programa principal se ejecuta el código dentro del condicional.
    iniciarInterfaz()