############################
# Importación de librerias # 
############################

from generarArchivos import *
from tkinter import *
from funciones import *
from archivos import *
from tkinter import messagebox, ttk
from claseCliente import *


############################
#    Variables globales    # 
############################

dicBD = {}
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

def crearEntradaTexto(pventana, ptexto, pvariable, pjustify,pfont='arial',psize=12,pbg='#f0f0f0',pfg='black',pstate=NORMAL):
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
    entrada = ttk.Entry(pventana, textvariable= pvariable, justify = pjustify,state=pstate)
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
    ventana.resizable(0,0)
    ventana.iconbitmap("icon.ico")
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

########################################### Cargar códigos ##################################################    
def cargarCodPostales():
    dicBD.update(crearBDCodigos())
    return dicBD

def abrirVentanaCargarCodigos(pventana, pboton, pfuncion):
    """
    Funcionalidad: Al presionar el botón de extraer frases se abre esta abre una ventana que muestra un mensaje
    Entradas: Na 
    Salidas: Na
    """
    codigosPostalesDinamico = cargarCodPostales()
    if codigosPostalesDinamico == False:
        return mostrarError(pventana, "Error\nNo se ha encontrado el archivo que contiene los códigos postales.\nEl archivo se debe llamar: BDPostalCR.txt.")
    pboton.config(state="disabled")
    pfuncion()
    mostrarInfo(pventana, "Se han cargado los códigos exitosamente.")
    return ""
########################################### Insertar cliente ##################################################    
def validarEstado(pcombo, pcomboNext, flag=True):
    if pcombo.get() == "— Provincias —" or pcombo.get()=="— Cantones Disponibles —":
        pcomboNext.config(state="disabled")
        return ""
    pcomboNext.config(state="readonly")
    return ""

def deNumAProvincia(pprovincia, pcombo, pcomboNext):
    """
    Función:    Busca una provincia a partir del número de la caja de selección
    Entradas:   pventana ,pprovincia(Str),pcanton(str),pnum(int)
    Salidas:    Retorna una provincia str
    """
    if pprovincia == "— Provincias —":
        pcombo.config(state="disabled")
        pcomboNext.config(state="disabled")
        return ""
    pcomboNext.config(state="readonly")
    return conseguirCantones(dicBD, pprovincia)

def deProvinciaACantonAux(pprovincia, pcanton, pcombo):
    """
    Función:    Busca un cantón a partir de la provincia y número de caja
    Entradas:   pventana ,pprovincia(Str),pnum(int)
    Salidas:    Retorna un cantón str
    """
    if pcanton == "— Cantones Disponibles —":
        pcombo.config(state="disabled")
        return ""
    pcombo.config(state="readonly")
    return conseguirDistritos(dicBD, pprovincia, pcanton)

########################################### Insertar cliente ##################################################    
def validarRegistrarCliente(pventana, pcedula,pnombre,pespe,pprovin,pcan,pdis,pcorreo, pfuncion):
    listaGen = [pprovin,pcan,pdis]
    pespe = validar60(pespe)
    pnombre = validarNombre(pnombre)
    if validarCedula(pcedula)== False:
        return mostrarError(pventana, "El formato de cédula debe ser: #(1-9)-#####-####")
    elif encontrarCedula(pcedula,clientes()):
        return mostrarError(pventana, "La cédula ingresada ya se encuentra ingresada.")
    elif pnombre == None:
        return mostrarError(pventana, "En el nombre debe ingresar 3 valores.")
    elif pnombre == False:
        return mostrarError(pventana, "El nombre debe contener solo letras.")
    elif pespe == None:
        return mostrarError(pventana, "Se debe ingresar 3 valores:\n'Calle Avenida #' (Separados por espacios)")
    elif pespe==False :
        return mostrarError(pventana, "Los valores de 'Calle Avenida #' deben ser mayores a 0 y menores que 61.")
    elif pprovin == "— Provincias —":
        return mostrarError(pventana, "Escoja una provincia.")
    elif pcan == "— Cantones Disponibles —":
        return mostrarError(pventana, "Escoja un cantón.")
    elif pdis == "— Distritos Disponibles —":
        return mostrarError(pventana, "Escoja un distrito.")
    elif validarCorreo(pcorreo) == False:
        return mostrarError(pventana, "El correo no debe llevar tildes y debe ser con dominio @gmail.com")
    elif encontrarCorreo(pcorreo,clientes()):
        pcorreo = generarCorreo(pnombre, False)
        mostrarInfo(pventana, f"El correo ingresado ya se ha registrado.\nSu nuevo correo será {pcorreo}.")
    codigo = conseguirCodigo(dicBD, pprovin, pcan, pdis)
    clienteN = Cliente()
    clienteN.asignarCedula(str(pcedula)),clienteN.asignarNombre(pnombre),clienteN.asignarDirEspecifica(pespe)
    clienteN.asignarDirGeneral(listaGen),clienteN.asignarCorreo(pcorreo),clienteN.asignarCodigoPostal(codigo)
    listaClientes = clientes()
    listaClientes.append(clienteN)
    grabarBinario('ClientesBD',listaClientes)
    pfuncion()
    return mostrarInfo(pventana, "Cliente ingresado satisfactoriamente.")

def asignarPls(pentrada, pprov, pcan, pdis):
    a = StringVar(value=conseguirCodigo(dicBD, pprov.get(), pcan.get(), pdis.get()))
    pentrada.config(textvariable=a, state="readonly")
    return pentrada

def cajasGeneral(pventana):
    """
    Función:    Crea y actualiza valores de cajas de selección de frases
    Entradas:   pventana (tk.Toplevel) - Ventana de submenú
    Salidas:    Retorna objetos (ttk.Combobox) creados
    """
    provincias =  conseguirProvincias(dicBD)
    caja1 = crearCaja(pventana, "Provincias: ", tk.StringVar(), provincias, "center")
    caja2 = crearCaja(pventana, "Cantones: ", tk.StringVar(), None, "center")
    caja3 = crearCaja(pventana, "Distrito: ", tk.StringVar(), None, "center")
    entrada = tk.Entry(pventana)
    entrada.config(width=50, state="readonly")
    caja1.set("— Provincias —")
    activar = lambda e: validarEstado(caja1, caja2)
    funcion1 = lambda: (caja1.bind("<<ComboboxSelected>>", activar), caja2.set("— Cantones Disponibles —"), caja3.config(state="disabled"),
    caja3.set("— Distritos Disponibles —"), entrada.insert(0, asignarPls(entrada, caja1, caja2, caja3)))
    activar2 = lambda e: validarEstado(caja2, caja3)
    funcion2 = lambda: (caja2.config(values = deNumAProvincia(caja1.get(), caja2, caja3)), caja3.set("— Distritos Disponibles —"), 
    caja2.bind("<<ComboboxSelected>>", activar2), entrada.insert(0, asignarPls(entrada, caja1, caja2, caja3)))
    funcion = lambda e: entrada.insert(0, asignarPls(entrada, caja1, caja2, caja3))
    funcion3 = lambda: (caja3.config(values=conseguirDistritos(dicBD, caja1.get(), caja2.get())), 
    caja3.bind("<<ComboboxSelected>>", funcion))
    caja1.config(width = "72", postcommand = funcion1)
    caja2.config(width="72", postcommand=funcion2, state="disabled")
    caja3.config(width="72", postcommand=funcion3, state="disabled")
    entrada.pack()
    return caja1, caja2 , caja3, entrada

def colocarComponentesVentanaInsertarCliente(ventanaInsertarCliente, pfuncion):
    """
    Funcionalidad: Coloca los componentes(cajas de texto,labels, caja de seleccion) en la ventana
    de insertar estudiante.
    Entradas: La ventana en la que se van a unicar los componentes(VentanaInsertarEstudiante)
    Salidas: Na 
    """
    cedula = crearEntradaTexto(ventanaInsertarCliente, "Cédula: ", tk.StringVar(), "center",psize=10)
    nombre = crearEntradaTexto(ventanaInsertarCliente, "Nombre: ", tk.StringVar(), "center",psize=10)
    nombre.config(width=40)
    uEspecifica=crearEntradaTexto(ventanaInsertarCliente, "Ubicación Específica: ", tk.StringVar(), "center",psize=10)
    cajaPro,cajaCan,cajaDis, entrada = cajasGeneral(ventanaInsertarCliente)
    correo=crearEntradaTexto(ventanaInsertarCliente, "Correo Electronico: ", tk.StringVar(), "center",psize=10)
    correo.config(width=40)
    correo.pack()
    funcion = lambda:validarRegistrarCliente(ventanaInsertarCliente,cedula.get(),nombre.get(),uEspecifica.get(),cajaPro.get(),cajaCan.get(),cajaDis.get(),correo.get(), pfuncion)
    botonInsertar=crearBoton(ventanaInsertarCliente,'Ingresar Cliente',funcion)
    
def abrirVentanaIngresarCliente(pventana, pfuncion):
    """
    Funcionalidad: Al presionar el botón de insertar estudiante se abre esta ventana, la cual contiene cajas de texto
    menú de selección para ingresar los datos.
    Entradas: Na 
    Salidas: Na 
    """
    ventanaInsertarCliente = tk.Toplevel(pventana)
  # Configuracion de la ventana secundaria
    ventanaInsertarCliente.title("Registrar Cliente")
    ventanaInsertarCliente.lift(pventana)  # Posiciona por encima de ventana principal
    dimensionarVentana(ventanaInsertarCliente, 350, 600)
    colocarComponentesVentanaInsertarCliente(ventanaInsertarCliente, pfuncion)
    ventanaInsertarCliente.mainloop()
########################################### Ventana crear clientes ##################################################    
def validarRegistrarClientes(pventana, pnum, pfuncion):
    listaClientes, dicCodigos, pnum = clientes(), dicBD, esEntero(pnum)
    if pnum == None:
        return mostrarError(pventana, "Solo se deben ingresar números enteros.")
    elif pnum == 0:
        return mostrarError(pventana, "Se debe ingresar un número mayor a 0.")
    grabarBinario("ClientesBD", crearClientes(pnum, listaClientes, dicCodigos))
    pfuncion()
    return mostrarInfo(pventana, "Base de datos creada.")

def entradasRegistrarClientes(pventana, pfuncion):
    cantidadClientes = crearEntradaTexto(pventana, "Cantidad de clientes: ", tk.IntVar(), "center")
    funcion = lambda: validarRegistrarClientes(pventana, cantidadClientes.get(), pfuncion)
    botonIngresar = crearBoton(pventana, "Crear", funcion)

def menuRegistrarClientes(pprincipal, pfuncion):
    """
    Funcionalidad: Al presionar el botón de insertar n grupos en la ventana principal, smenuRegistrarClientese abre o crea otra ventana 
    que me permite ingresar la información requerida
    Entradas: Na 
    Salidas: Na 
    """
    ventana = tk.Toplevel(pprincipal)
    # Configuracion de la ventana secundaria
    ventana.title("Crear clientes")
    ventana.lift(pprincipal)    # Posiciona por encima de ventana principal
    dimensionarVentana(ventana, 350, 100)
    entradasRegistrarClientes(ventana, pfuncion)
    
###########################################   exportar   ##################################################
def exportarXML():
    dicCodigos = dicBD
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
    listClientes = clientes()
    provincias = crearListProvDisp(listClientes)
    cajaProv = crearCaja(pventana, "Escoja una provincia", tk.StringVar(), provincias, "center")
    cajaProv.set("- Provincias -")
    funcion = lambda: validarReporteProvincia(pventana, cajaProv.current(), provincias)
    boton = crearBoton(pventana, "Crear reporte", funcion)
    
def ventanaReporteProvincia(pventana):
    ventana = tk.Toplevel(pventana)
    # Configuracion de la ventana secundaria
    ventana.title("Reporte según provincia")
    ventana.lift(pventana)    # Posiciona por encima de ventana principal
    dimensionarVentana(ventana, 350, 200)
    entradasReporteProvincia(ventana)   # Crea y valida entradas
########################################### Etiqueta ##################################################    
def asignarNombre(pcedula):
    """
    F: asigna nombre
    E: cedula
    S:nombre
    """
    try:
        tupla = deCedulaATupla(clientes(),pcedula)
        return mostrarNombreCliente(tupla[0])
    except:
        return mostrarError(None, "Por favor seleccione a un cliente")
def rellenarEntradasEtiqueta(pventana, pentradaGen, pentradaEspe, pentradaCod, pcedula):
    try:
        tupla = deCedulaATupla(clientes(),pcedula)
        a = StringVar(value=tupla[3])
        pentradaCod.config(textvariable=a, state="readonly")
        a = StringVar(value=mostrarDirGeneral(tupla[2]))
        pentradaGen.config(textvariable=a, state="readonly")
        a = StringVar(value=tupla[1])
        pentradaEspe.config(textvariable=a, state="readonly")
        return pentradaGen, pentradaEspe, pentradaCod
    except:
        return mostrarError(pventana,'Seleccione una cédula')
def generarEtiquetaTK(pventana, pcedula, pdirGen, pdirEspe, pcodigo):
    try:
        nombre = mostrarNombreCliente(deCedulaATupla(clientes(), pcedula)[0])
        creaPdf(nombre, pdirEspe, pdirGen, pcodigo)
        return ""
    except:
        return mostrarError(pventana, "Por favor seleccione algún cliente.")
def entradasEtiqueta(pventana):
    """
    F: ingresa a la ventana los botones y cajas de seleccion 
    E: ventana
    S: N/A
    """
    listaClientes= listaCedNom(clientes())
    cajaCli = crearCaja(pventana, "Escoja un cliente", tk.StringVar(), listaClientes, "center")
    cajaCli.config(width=75)
    cajaCli.set("- Clientes -")
    entrada1, entrada2, entrada3 = tk.Entry(pventana), tk.Entry(pventana), tk.Entry(pventana)
    for elem in (entrada1, entrada2, entrada3):
        elem.config(state="readonly", width=40)
        elem.pack(padx=10, pady=10)
    tupla = lambda: rellenarEntradasEtiqueta(pventana, entrada1, entrada2, entrada3, tomarHastaCaracter(cajaCli.get(), ">"))
    funcion0 = lambda e: (entrada1.insert(0, tupla()[0]), entrada2.insert(0, tupla()[1]), entrada3.insert(0, tupla()[2]))
    funcion = lambda : cajaCli.bind("<<ComboboxSelected>>", funcion0)
    cajaCli.config(postcommand=funcion)
    funcion4 = lambda: generarEtiquetaTK(pventana, tomarHastaCaracter(cajaCli.get(), ">"), entrada1.get(), entrada2.get(), entrada3.get())
    botonInsertar=crearBoton(pventana,'Generar etiqueta',funcion4)

###########################
# Reporte según cédula    #
###########################
def validarReporteCedula(pventana, pcedula):
    listaClientes = clientes()
    pcedula = validarCedula(pcedula)
    if pcedula == False:
        return mostrarError(pventana, "El formato de cédula debe ser: #(1-9)-#####-####")
    elif not encontrarCedula(pcedula, listaClientes):
        return mostrarInfo(pventana, "La cédula ingresada todavía no ha sido registrada.")
    return crearReporteCliente(pcedula, listaClientes)

def entradasReporteCedula(pventana):
    cedula = crearEntradaTexto(pventana, "Ingrese la cédula", tk.StringVar(), "center")
    funcion = lambda: validarReporteCedula(pventana, cedula.get())
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
def validarReporteCodigo(pventana, pcodigo, plistaCodDisp):
    listaClientes = clientes()
    if pcodigo == -1:
        return mostrarError(pventana, "Por favor escoja un código")
    crearReporteCodPostal(tomarHastaCaracter(plistaCodDisp[pcodigo], ":").strip(), listaClientes)
    return ""
    
def entradasReporteCodigo(pventana):
    listaClientes = clientes()
    codigosActu = listaCodDirEspe(listaClientes)
    caja = crearCaja(pventana, "Códigos disponibles", tk.StringVar(), codigosActu, "center")
    caja.config(width=60)
    caja.set("- Códigos -")
    funcion = lambda: validarReporteCodigo(pventana, caja.current(), codigosActu)
    boton = crearBoton(pventana, "Generar reporte", funcion)

def ventanaReporteCodigo(pventana):
    ventana = tk.Toplevel(pventana)
    ventana.title("Reporte según código postal")
    ventana.lift(pventana)
    dimensionarVentana(ventana, 400, 250)
    entradasReporteCodigo(ventana)
#######################
# Submenu de reportes #
#######################
def botonesMenuReportes(pventana):
    funcionProvincia = lambda: ventanaReporteProvincia(pventana)
    funcionCedula = lambda: ventaReporteCedula(pventana)
    funcionCodigo = lambda: ventanaReporteCodigo(pventana)
    botonProvincia = crearBoton(pventana, "Reportes Según Provincia", funcionProvincia)
    botonCedula = crearBoton(pventana, "Reporte según cédula", funcionCedula)
    botonCodigo = crearBoton(pventana, "Reporte según código", funcionCodigo)

def subMenuReportes(pventana):
    ventana = tk.Toplevel(pventana)
    ventana.title("Menú de reportes")
    ventana.lift(pventana)
    dimensionarVentana(ventana, 300, 200)
    botonesMenuReportes(ventana)
    
def abrirVentanaPdfEtiqueta(pprincipal):
    """
    Funcionalidad: Genera una etiqueta
    Entradas: Na 
    Salidas: reporte pdf 
    """
    ventana = tk.Toplevel(pprincipal)
    ventana.title('Ventana Generar Etiqueta')
    ventana.geometry('500x500')
    ventana.resizable(0,0)
    ventana.iconbitmap('icon.ico')
    ventana.lift(pprincipal)    # Posiciona por encima de ventana principal
    dimensionarVentana(ventana, 300, 300)
    entradasEtiqueta(ventana)
########################################### Enviar correo ##################################################    
def validarCedulaCorreo(pventana, pcedula):
    """
    F: Valida la cedula si esta repetida o si la no tiene formato correcto
    E: ventana y cedula(str)
    S:N/A
    """
    lista = deCedulaATupla(clientes(),pcedula)
    if validarCedula(pcedula)==False:
        return mostrarError(pventana, "El formato de cédula debe ser: #(1-9)-#####-####")
    elif lista == False:
        return mostrarError(pventana, "La cédula ingresada todavía no ha sido registrada.")
    enviarCorreo(lista[-1],lista[0])
    return mostrarInfo(pventana,'Se ha enviado Correo')

        #return mostrarError(pventana,'El correo no se pudo enviar')

def entradaEnviarCorreo(pventana):
    """
    F: ingresa a la ventana los botones y cajas de seleccion 
    E: ventana
    S: N/A
    """
    cedula = crearEntradaTexto(pventana, "Ingrese su número de cédula: ", tk.StringVar(), "center")
    funcion = lambda: validarCedulaCorreo(pventana, cedula.get())
    botonIngresar = crearBoton(pventana, "Buscar Info", funcion)

def abrirVentanaEnviarCorreo(pprincipal):
    ventana = tk.Toplevel(pprincipal)
    ventana.title('Enviar Correos')
    ventana.lift(pprincipal)    # Posiciona por encima de ventana principal
    dimensionarVentana(ventana, 300, 100)
    entradaEnviarCorreo(ventana)
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
    ventana.config(bg='black')
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
########################################### Ventana principal ##################################################    
def colocarBotonesPrincipal(ventanaPrincipal):
    """
    Funcionalidad: Coloca los botones en la ventana principal 
    Entradas: La ventana principal 
    Salidas: Na (interfaz)
    """
    nombresBotones = ("1. códigos postales.", "2. Registrar Cliente.", "3. Crear Clientes.", "4. Generar Etiqueta.",
    "5. Enviar Correo.", "6. Exportar Códigos.", "7. Reportes.", "8. Credenciales.", "9. Salir.")        
    funciones = (lambda: None, 
                lambda: None, lambda: abrirVentanaPdfEtiqueta(ventanaPrincipal), 
                lambda: abrirVentanaEnviarCorreo(ventanaPrincipal), lambda: exportarXML(), 
                lambda: subMenuReportes(ventanaPrincipal))
    botonCargarCodigos = crearBoton(ventanaPrincipal, nombresBotones[0], None)
    botonRegistraCliente = crearBoton(ventanaPrincipal, nombresBotones[1], funciones[0])
    botonInsertarClientes = crearBoton(ventanaPrincipal, nombresBotones[2], funciones[1])
    botonCrearEtiqueta = crearBoton(ventanaPrincipal, nombresBotones[3], funciones[2])
    botonEnviarCorreo =  crearBoton(ventanaPrincipal, nombresBotones[4], funciones[3])
    botonExportarCodigos = crearBoton(ventanaPrincipal, nombresBotones[5], funciones[4])
    botonCrearReportes = crearBoton(ventanaPrincipal, nombresBotones[6], funciones[5])
    botonCredenciales = crearBoton(ventanaPrincipal, nombresBotones[7], None)
    botonSalir = crearBoton(ventanaPrincipal, nombresBotones[-1], ventanaPrincipal.destroy)
    return botonCargarCodigos, botonRegistraCliente, botonInsertarClientes, botonCrearEtiqueta, botonEnviarCorreo, botonExportarCodigos, botonCrearReportes, botonCredenciales

def activarBotones(pBotones,pdicBD = dicBD):
    activar2 = list(pBotones[:2]) + [pBotones[4]]
    for boton in pBotones:
        if pdicBD != {} and clientes() != []:
            boton.config(state="normal")
        elif pdicBD != {} and clientes()==[]:
            for boton2 in activar2:
                boton2.config(state="normal")
                return ""
        else:
            boton.config(state="disabled")
    return ""

def activarBoton(pdatos):
    """
    Función:    Genera estado activo para boton si no existe una BD
    Entradas:   pdatos (list) - Variable que lee una BD
    Salidas:    Retorna "normal" si no existe, "disabled" si ya existe BD
    """
    if pdatos == {}:
        return "normal"
    return "disabled"

def configPrincipal(pventana, pbotones):
    funcionActivar = lambda: activarBotones(pbotones[1:-1])
    funcionCodPostales = lambda: (abrirVentanaCargarCodigos(pventana, pbotones[0], funcionActivar), cargarCodPostales())
    funcionCredenciales = lambda: abrirVentanaCredenciales(pventana)
    funcionRegistrarCliente = lambda: abrirVentanaIngresarCliente(pventana, funcionActivar)
    funcionGenerarClientes = lambda: menuRegistrarClientes(pventana, funcionActivar)
    pbotones[0].config(state=activarBoton(dicBD), command=funcionCodPostales)
    pbotones[-1].config(state="normal", command=funcionCredenciales)
    pbotones[1].config(command=funcionRegistrarCliente)
    pbotones[2].config(command=funcionGenerarClientes)
    funcionActivar()
    return ""

def iniciarInterfaz():
    """
    Funcionalidad: Crea la ventxana principal que contendrá los botones principales 
    Entradas: Na 
    Salidas: Na 
    """
    ventanaPrincipal = crearVentana("Correos Costa Rica")
    dimensionarVentana(ventanaPrincipal, 370, 520)
    configPrincipal(ventanaPrincipal, colocarBotonesPrincipal(ventanaPrincipal))
    #colocarBotonesPrincipal(ventanaPrincipal)
    ventanaPrincipal.mainloop()
iniciarInterfaz()
#print(leerBinarioLista('ClientesBD'))