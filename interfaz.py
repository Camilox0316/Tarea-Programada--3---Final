############################
# Importación de librerias # 
############################
from tkinter import *
from tkinter.font import BOLD
from funciones import *
from archivos import *

############################
#    Variables globales    # 
############################

dicBD = crearBDCodigos()


############################
# Definición de Funciones  # 
############################

#   ------------------------------------------------- Formato general  -------------------------------------------------
def crearVentana(titulo):
    """
    Funcionalidad: Formato general para crear una nueva ventana 
    Entradas: titulo: Nombre de la ventana 
    Salidas: Ventana en la interfaz 
    """
    ventana = Tk()
    ventana.title(titulo)
    ventana.resizable(False,False)
    ventana.config(bg = '#ffffff')
    ventana.iconbitmap('icon.ico')
    ventana.update()
    return ventana

def crearVentanaSecundaria(titulo): 

    ventanaSecundaria = Toplevel()
    ventanaSecundaria.title(titulo)
    ventanaSecundaria.resizable(False,False)
    ventanaSecundaria.config(bg = '#153a7a')
    ventanaSecundaria.iconbitmap('icon.ico')
    return ventanaSecundaria  

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

#   ------------------------------------------------- VENTANA PRINCIPAL -------------------------------------------------

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

def colocarBotonesVentanaPrincipal(ventanaPrincipal):
    """
    Funcionalidad: Coloca los botones en la ventana principal 
    Entradas: La ventana principal 
    Salidas: Na (interfaz)
    """
    global botonCargarCodigos 
    global botonRegistrarCliente
    global botonInsertarClientes
    global botonEtiquieta  
    global botonCorreo
    global botonExportarCodigo
    global botonReportes 
    global botonCredenciales
    global label

    botonCargarCodigos = Button(ventanaPrincipal,text="1. Cargar Códigos Postales.",command= abrirVentanaCargarCodigos)
    botonCargarCodigos.config(width = "25",fg="white", font= ("Arial", 12,BOLD),bg='#64fa6e')
    botonCargarCodigos.pack(padx=30, pady=10)

    botonRegistrarCliente = Button(ventanaPrincipal,text="2. Registrar Cliente.", command=abrirVentanaIngresarCliente)
    botonRegistrarCliente.config(width = "25",fg="white",font= ("Arial", 12,BOLD),bg='#64fa6e')
    botonRegistrarCliente.pack(padx=30, pady=10)

    botonInsertarClientes = Button(ventanaPrincipal,text="3. Crear Clientes.", command=abrirVentanaLabelInsertarClientes)
    botonInsertarClientes.config(width = "25",fg="white",font= ("Arial", 12,BOLD),bg='#64fa6e')
    botonInsertarClientes.pack(padx=30, pady=10)

    botonEtiqueta = Button(ventanaPrincipal,text="4. Generar Etiquieta.", command='')
    botonEtiqueta.config(width = "25",fg="white",font= ("Arial", 12,BOLD),bg='#64fa6e')
    botonEtiqueta.pack(padx=30, pady=10)

    botonCorreo = Button(ventanaPrincipal,text="5. Enviar Correo.", command='')
    botonCorreo.config(width = "25",fg="white",font= ("Arial", 12,BOLD),bg='#64fa6e')
    botonCorreo.pack(padx=30, pady=10)

    botonExportarCodigo = Button(ventanaPrincipal,text="6. Exportar Códigos.", command='')
    botonExportarCodigo.config(width = "25",fg="white",font= ("Arial", 12,BOLD),bg='#64fa6e')
    botonExportarCodigo.pack(padx=30, pady=10)

    botonReportes = Button(ventanaPrincipal,text="7. Reportes.")
    botonReportes.config(width = "25",fg="white",font= ("Arial", 12,BOLD),bg='#64fa6e', command=abrirVentanaReportes)
    botonReportes.pack(padx=30, pady=10)

    botonCredenciales = Button(ventanaPrincipal,text="8. Credenciales.")
    botonCredenciales.config(width = "25",fg="white",font= ("Arial", 12,BOLD),bg='#64fa6e',command=abrirVentanaCredenciales)
    botonCredenciales.pack(padx=30, pady=10)

    botonSalir = Button(ventanaPrincipal,text="9. Salir.")
    botonSalir.config(width = "25",fg="white",font= ("Arial", 12,BOLD),bg='#64fa6e', command=ventanaPrincipal.destroy)
    botonSalir.pack(padx=30, pady=10)

    #if verificarArchivo("frasesMotivadoras") and verificarArchivo("bitacora estudiantil"):
    #    botonExtraerFrases.config(state = NORMAL)
    #    botonInsertarGrupos.config(state = DISABLED)
    #    botonInsertarEstudiante.config(state = DISABLED)
    #    botonAgregarFrase.config(state = DISABLED)
    #    botonEliminarEstudiante.config(state = DISABLED)
    #    botonReportes.config(state = DISABLED)
    #elif not verificarArchivo("frasesMotivadoras") and verificarArchivo("bitacora estudiantil"): 
    #    botonExtraerFrases.config(state = DISABLED)
    #    botonInsertarGrupos.config(state = NORMAL)
    #    botonInsertarEstudiante.config(state = DISABLED)
    #    botonAgregarFrase.config(state = DISABLED)
    #    botonEliminarEstudiante.config(state = DISABLED)
    #    botonReportes.config(state = DISABLED)
    #else: 
    #    botonExtraerFrases.config(state = DISABLED)
    #    botonInsertarGrupos.config(state = DISABLED)
    #    botonInsertarEstudiante.config(state = NORMAL)
    #    botonAgregarFrase.config(state =NORMAL)
    #    botonEliminarEstudiante.config(state = NORMAL)
    #    botonReportes.config(state = NORMAL)

#   ------------------------------------------------- VENTANA Cargar Códigos -------------------------------------------------

def abrirVentanaCargarCodigos():
    """
    Funcionalidad: Al presionar el botón de extraer frases se abre esta abre una ventana que muestra un mensaje
    Entradas: Na 
    Salidas: Na
    """
    global botonExtraerFrases        
    global botonInsertarGrupos 
    ventanaExtraerCodigos = crearVentanaSecundaria("Cargar Códigos Postales")
    dimensionarVentana(ventanaExtraerCodigos, 350, 100)
    leerTXT('BDPostalCR.txt') 
    colocarLabelVentanaCargarCodigos(ventanaExtraerCodigos)
    ventanaExtraerCodigos.mainloop()

def colocarLabelVentanaCargarCodigos(ventanaExtraerCodigos):
    """
    Funcionalidad: Muestra una pequeña ventana indicando un mensaje de que se han almacenado las frases en la BD 
    Entradas: VentanaExtraerFrases
    Salidas: Una ventana con mensaje 
    """
    labelInforme = Label(ventanaExtraerCodigos, text="Se han Cargado los códigos \nExitosamente")
    labelInforme.pack(padx=20, pady=30)
    labelInforme.config(fg='white',font=('Helvatical bold', 13), bg = '#153a7a')


#   ------------------------------------------ VENTANA INSERTAR ClIENTE -------------------------------------------------

def abrirVentanaIngresarCliente():
    """
    Funcionalidad: Al presionar el botón de insertar estudiante se abre esta ventana, la cual contiene cajas de texto
    menú de selección para ingresar los datos.
    Entradas: Na 
    Salidas: Na 
    """
    ventanaInsertarCliente = crearVentanaSecundaria("Insertar estudiante")
    dimensionarVentana(ventanaInsertarCliente,350,500)
    colocarComponentesVentanaInsertarEstudiante(ventanaInsertarCliente)
    ventanaInsertarCliente.mainloop()

def colocarComponentesVentanaInsertarEstudiante(ventanaInsertarCliente):
    """
    Funcionalidad: Coloca los componentes(cajas de texto,labels, caja de seleccion) en la ventana
    de insertar estudiante.
    Entradas: La ventana en la que se van a unicar los componentes(VentanaInsertarEstudiante)
    Salidas: Na 
    """
    labelCedula = Label(ventanaInsertarCliente, text="Cédula:")
    labelCedula.pack(padx=20, pady=10)
    labelCedula.config(fg='white',font=('Helvatical bold', 12), bg = '#153a7a')
    entryCedula = Entry(ventanaInsertarCliente, width=100, justify="center")
    entryCedula.config(font=('Helvatical bold', 10))
    entryCedula.pack(padx=30, pady=0)

    labelNombre = Label(ventanaInsertarCliente, text="Nombre:")
    labelNombre.pack(padx=20, pady=10)
    labelNombre.config(fg='white',font=('Helvatical bold', 12), bg = '#153a7a')
    entryNombre = Entry(ventanaInsertarCliente, width=100, justify="center")
    entryNombre.config(font=('Helvatical bold', 10))
    entryNombre.pack(padx=30, pady=0)
    try: 
        Provincias =  conseguirProvincias(dicBD)
        ProvinciaSeleccionada = StringVar(ventanaInsertarCliente) #StrVar declara una variable de tipo cadena
        ProvinciaSeleccionada.set("Seleccione una Provincia:")
        # .set() asigna un valor a una variable de control. Se utiliza para modificar el valor o estado de un widged
        Cantones = [""] 
        CantonSeleccionado = StringVar(ventanaInsertarCliente)
        CantonSeleccionado.set("Seleccione un Cantón:")
        cajaSeleccionCanton = OptionMenu(ventanaInsertarCliente, CantonSeleccionado, *Cantones)
        cajaSeleccionProvincia = OptionMenu(ventanaInsertarCliente, ProvinciaSeleccionada, *Provincias, 
        command=lambda ProvinciaSeleccionada: actualizarFrasesMostrar(ProvinciaSeleccionada, cajaSeleccionCanton, CantonSeleccionado))
        cajaSeleccionProvincia.pack(padx=20, pady=30)
        cajaSeleccionCanton.pack(padx=20, pady=0)

        Distritos = [""] 
        DistritoSeleccionado = StringVar(ventanaInsertarCliente)
        DistritoSeleccionado.set("Seleccione un Distrito: ")
        cajaSeleccionDistrito = OptionMenu(ventanaInsertarCliente, DistritoSeleccionado, *Distritos)
        cajaSeleccionDistrito.pack(padx=20, pady=30)

        botonInsertarEstudiante = Button(ventanaInsertarCliente,text="Insertar Estudiante", 
        command=lambda:abrirVentanaLabelInsertarEtudiante(entryCedula.get(),entryNombre.get(),ProvinciaSeleccionada.get(), CantonSeleccionado.get(), DistritoSeleccionado.get()))
        botonInsertarEstudiante.config(width = "25",fg="black",font= ("Arial", 12))
        botonInsertarEstudiante.pack(padx=30, pady=0)
    except: 
        mostrarLabelError()

def insertarEstudiante(carnet, nombre,categoria, frase, grupo):
    """
    Funcionalidad: Inserta un estudiante con todos los datos en la bitacora estudiantil
    Entradas: carnet(str): del estudiante
    nombre(str): Nombre del estudiante 
    categoria(str): categoria seleccionada
    frase(str): frase de la categoría seleccionada 
    grupo(str): Grupo en el que se va a ubicar el estudiante. 
    Salidas: Na 
    """
    lista = list(lee('bitacora estudiantil'))
    if validarCedula(str(carnet)):
        if validarNombre(nombre):
            lista.append([int(carnet),tuple(nombre.split()), [deFraseATupla(categoria, frase)], int(grupo)])
            graba('bitacora estudiantil',lista)
            print([int(carnet),tuple(nombre.split()),[frase], int(grupo)])
          
def abrirVentanaLabelInsertarEtudiante(carnet, nombre,categoria, frase, grupo):
    """
    Funcionalidad: Valida que se ingresen los datos correctos antes de registrar el estudiante en la bitacora.
    Entradas: carnet(str): del estudiante
    nombre(str): Nombre del estudiante 
    categoria(str): categoria seleccionada
    frase(str): frase de la categoría seleccionada 
    grupo(str): Grupo en el que se va a ubicar el estudiante. 
    Salidas: Na
    """
    ventanaLabelInsertarEstudiante = crearVentanaSecundaria("Insertar un Estudiante")
    dimensionarVentana(ventanaLabelInsertarEstudiante, 350, 250)
    if validarCarne(carnet):
        if not verificarCarnet(int(carnet)):
            if validarNombre(nombre):
                if categoria != "Seleccione una categoría": 
                    if frase != "Seleccione una frase": 
                        if grupo != "Seleccione un grupo": 
                            insertarEstudiante(carnet, nombre,categoria, frase, grupo)
                            confirmacionEstudianteInsertado(ventanaLabelInsertarEstudiante,ventanaLabelInsertarEstudiante)                        
                        else: 
                            labelGrupoInvalido(ventanaLabelInsertarEstudiante)
                    else:
                        labelFraseInvalida(ventanaLabelInsertarEstudiante)
                else:
                    labelCategoriaInvalida(ventanaLabelInsertarEstudiante)
            else:
                labelNombreInvalido(ventanaLabelInsertarEstudiante)
        else: 
            labelCarneRepetido(ventanaLabelInsertarEstudiante)
    else: 
        labelCarnetInvalido(ventanaLabelInsertarEstudiante)
    ventanaLabelInsertarEstudiante.mainloop()

def confirmacionEstudianteInsertado(ventanaLabelInsertarEstudiante,ventanaInsertarEstudiante):
    """
    Funcionalidad: Muestra una pequeña ventana indicando un mensaje de que se ha insertado el estudiante correctamente
    Entradas: Ventana insertar Estudiante 
    Salidas: Una ventana con mensaje 
    """
    labelInforme = Label(ventanaLabelInsertarEstudiante, text="Se ha insertado el estudiante \nen la bitácora estudiantil'")
    labelInforme.pack(padx=20, pady=30)
    labelInforme.config(font=('Helvatical bold', 13), bg = '#6fabaa')

    botonOk = Button(ventanaLabelInsertarEstudiante,text="Ok", command =ventanaLabelInsertarEstudiante.destroy )
    botonOk.config(width = "25",fg="black",font= ("Arial", 12))
    botonOk.pack(padx=30, pady=20)

def labelCarnetInvalido(ventanaLabelInsertarEstudiante):
    """
    Funcionalidad: Muestra un mensaje indicando que el carnet no es válido.
    Entradas: ventanaLabelInsertarEstudiante 
    Salidas: Una ventana con mensaje 
    """
    labelInforme = Label(ventanaLabelInsertarEstudiante, text= "El carné no cumple con el formato: \n 202100####, significa: año, sede y aleatorio")
    labelInforme.pack(padx=20, pady=30)
    labelInforme.config(font=('Helvatical bold', 13), bg = '#6fabaa')

def labelNombreInvalido(ventanaLabelInsertarEstudiante):
    """
    Funcionalidad: indica un mensaje de que el nombre es invalido 
    Entradas: ventanaLabelInsertarEstudiante 
    Salidas: Una ventana con mensaje 
    """
    labelInforme = Label(ventanaLabelInsertarEstudiante, text= "Debe ingresar el nombre completo \n (Nombre Apellido1 Apellido2)")
    labelInforme.pack(padx=20, pady=30)
    labelInforme.config(font=('Helvatical bold', 13), bg = '#6fabaa')

def labelCategoriaInvalida(ventanaLabelInsertarEstudiante):
    """
    Funcionalidad: Indica un mensaje de eror si no se selecciona la categoría
    Entradas: ventanaLabelInsertarEstudiante
    Salidas: Una ventana con mensaje 
    """
    labelInforme = Label(ventanaLabelInsertarEstudiante, text= "Debe seleccionar una categoría. ")
    labelInforme.pack(padx=20, pady=30)
    labelInforme.config(font=('Helvatical bold', 13), bg = '#6fabaa')

def labelFraseInvalida(ventanaLabelInsertarEstudiante):
    """
    Funcionalidad: Indica un mensaje de error si no se selecciona la frase.
    Entradas:ventanaLabelInsertarEstudiante
    Salidas: Una ventana con mensaje 
    """
    labelInforme = Label(ventanaLabelInsertarEstudiante, text= "Debe seleccionar una frase")
    labelInforme.pack(padx=20, pady=30)
    labelInforme.config(font=('Helvatical bold', 13), bg = '#6fabaa')

def labelGrupoInvalido(ventanaLabelInsertarEstudiante):
    """
    Funcionalidad: Muestra un mensaje de error, si no se selecciona el grupo
    Entradas: Ventana insertar Estudiante 
    Salidas: Una ventana con mensaje 
    """
    labelInforme = Label(ventanaLabelInsertarEstudiante, text= "Debe seleccionar un grupo.")
    labelInforme.pack(padx=20, pady=30)
    labelInforme.config(font=('Helvatical bold', 13), bg = '#6fabaa')

def labelCarneRepetido(ventanaLabelInsertarEstudiante):
    """
    Funcionalidad: Indica un mensaje de error si el carné ya se encuentra registrado previamente.
    Entradas: Ventana insertar Estudiante 
    Salidas: Una ventana con mensaje 
    """
    labelInforme = Label(ventanaLabelInsertarEstudiante, text= "El carnet ya se encuentra registrado.")
    labelInforme.pack(padx=20, pady=30)
    labelInforme.config(font=('Helvatical bold', 13), bg = '#6fabaa')

def actualizarFrasesMostrar(provincia, cajaSeleccionFrases, cantones):
    """
    Funcionalidad: Actualiza las frases en la caja de seleccion, para que se muestren las que corresponden
    a la categoría seleccionada.
    Entradas: CategoriaSeleccionada, cajaSeleccionFrases, fraseSeleccionada
    Salidas: Actualiza la variable con las frases de la categoría seleccionada 
    """
    cantones = conseguirCantones(dicBD,provincia)
    for canton in cantones:
        cajaSeleccionFrases["menu"].add_command(label=canton, command=lambda canton=canton: cantones.set(canton))
#   ----------------------------------------- VENTANA CREAR CLIENTES -------------------------------------------------

def abrirVentanaRegistrarClientes():
    """
    Funcionalidad: Al presionar el botón de insertar n grupos en la ventana principal, se abre o crea otra ventana 
    que me permite ingresar la información requerida
    Entradas: Na 
    Salidas: Na 
    """
    ventanaRegistrarCliente = crearVentanaSecundaria("Crear Clientes")
    dimensionarVentana(ventanaRegistrarCliente, 350, 235)
    colocarComponentesVentanaRegistrarClientes(ventanaRegistrarCliente)
    ventanaRegistrarCliente.mainloop()

def colocarComponentesVentanaRegistrarClientes(ventanaInsertarClientes):
    """
    Funcionalidad: Coloca los label y cajas de texto en la ventana de insertar grupos 
    Entradas: Ventana a insertar los datos 
    Salidas: Na 
    """
    
    labelCantidadClientes = Label(ventanaInsertarClientes, text="Cantidad de Clientes:")
    labelCantidadClientes.pack(padx=20, pady=10)
    labelCantidadClientes.config(font=('Helvatical bold', 12), bg = '#153a7a')
    entryCantidadClientes = Entry(ventanaInsertarClientes, width=100, justify="center")
    entryCantidadClientes.config(font=('Helvatical bold', 10))
    entryCantidadClientes.pack(padx=30, pady=0)

    botonInsertarClientes = Button(ventanaInsertarClientes,text="Insertar Clientes", command=lambda:abrirVentanaLabelInsertarClientes(entryCantidadClientes.get()))
    botonInsertarClientes.config(width = "25",fg="white",font= ("Arial", 12))
    botonInsertarClientes.pack(padx=30, pady=30)

def insertarClientes(cantidadGrupos):
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

def abrirVentanaLabelInsertarClientes(cantidadClientes):
    """
    Funcionalidad: Al presionar el botón de insertar Grupos se abre esta abre una ventana que muestra un mensaje
    de realimentación o de error. 
    Entradas: Na 
    Salidas: Na
    """
    ventanaInsertarLabelClientes = crearVentanaSecundaria("Cantidad de Clientes")
    dimensionarVentana(ventanaInsertarLabelClientes, 400, 100)
    if verificarArchivo("BDPostalCR.txt"):    
        if insertarClientes(cantidadClientes): 
            LabelInsertarClientes(ventanaInsertarLabelClientes)
        else: 
            LabelNoInsertarClientes(ventanaInsertarLabelClientes)
    else: 
        LabelExtisteBD(ventanaInsertarLabelClientes)
    ventanaInsertarLabelClientes.mainloop()

def mostrarLabelError():
    ventanaError = crearVentanaSecundaria("Insertar un Estudiante")
    dimensionarVentana(ventanaError, 350, 250)
    labelInforme = Label(ventanaError, text="Favor reiniciar el programa.")
    labelInforme.pack(padx=20, pady=30)
    labelInforme.config(font=('Helvatical bold', 13), bg = '#153a7a')

def LabelExtisteBD(ventanaInsertarClientes):
    """
    Funcionalidad: Muestra una pequeña ventana indicando un mensaje de que se han almacenado las frases en la BD 
    Entradas: VentanaExtraerFrases
    Salidas: Una ventana con mensaje 
    """
    labelInforme = Label(ventanaInsertarClientes, text="Ya se encuentra una bitacora  \nregistrada.")
    labelInforme.pack(padx=20, pady=30)
    labelInforme.config(fg='white',font=('Helvatical bold', 13), bg = '#153a7a')

def LabelInsertarClientes(ventanaInsertarLabelGrupos):
    """
    Funcionalidad: Muestra una pequeña ventana indicando un mensaje de que se han almacenado las frases en la BD 
    Entradas: VentanaExtraerFrases
    Salidas: Una ventana con mensaje 
    """
    labelInforme = Label(ventanaInsertarLabelGrupos, text="Se han añadido \nlos clientes.")
    labelInforme.pack(padx=20, pady=30)
    labelInforme.config(fg='white',font=('Helvatical bold', 13), bg = '#153a7a')

def LabelNoInsertarClientes(ventanaInsertarLabelGrupos):
    """
    Funcionalidad: Muestra una pequeña ventana indicando un mensaje de que se han almacenado las frases en la BD 
    Entradas: VentanaExtraerFrases
    Salidas: Una ventana con mensaje 
    """
    labelInforme = Label(ventanaInsertarLabelGrupos, text="Ingrese valores númericos \nlos grupos deben ser mayor a 0.")
    labelInforme.pack(padx=20, pady=30)
    labelInforme.config(fg='white',font=('Helvatical bold', 13), bg = '#153a7a')
############################################## ETIQUIETA  ###############################################
def abrirVentanaPdfEtiqueta():
    """
    Funcionalidad: Genera una etiqueta
    Entradas: Na 
    Salidas: reporte pdf 
    """
    ventanaEtiqueta = crearVentana("Reporte PDF")
    dimensionarVentana(ventanaEtiqueta, 350, 160)
    # Meter una función que haga la etiqueta
    labelInforme = Label(ventanaEtiqueta, text="Se ha creado el reporte PDF \ncon éxito.")
    labelInforme.pack(padx=20, pady=30)
    labelInforme.config(font=('Helvatical bold', 13), bg = '#153a7a')

#   ---------------------------------------- VENTANA ELIMINAR ESTUDIANTE -------------------------------------------------
def abrirVentanaEliminarEstudiante():
    """
    Funcionalidad: Al presionar el botón de eliminar estudiante este crea una ventana con los componentes 
    para ingresar la información requerida
    Entradas: Na
    Salidas: Na ventana creada 
    """
    ventanaEliminarEstudiante = crearVentana("Eliminar estudiante")
    dimensionarVentana(ventanaEliminarEstudiante, 350, 300)
    colocarComponentesVentanaEliminarEstudiante(ventanaEliminarEstudiante)
    ventanaEliminarEstudiante.mainloop()

def colocarComponentesVentanaEliminarEstudiante(ventanaEliminarEstudiante):
    """
    Funcionalidad: Se colocan los componentes (entry y botón) en la ventana de eliminar estudiante 
    Entradas: Ventana en la que se van a colocar los componentes 
    Salidas: Na
    """
    labelCarnet = Label(ventanaEliminarEstudiante, text="Carnet:")
    labelCarnet.pack(padx=20, pady=10)
    labelCarnet.config(font=('Helvatical bold', 12), bg = '#6fabaa')
    entryCarnet = Entry(ventanaEliminarEstudiante, width=100, justify="center")
    entryCarnet.config(font=('Helvatical bold', 10))
    entryCarnet.pack(padx=30, pady=0)

    botonEliminarEstudiante = Button(ventanaEliminarEstudiante,text="Buscar estudiante", command=lambda: abrirVentanaConfirmacionEliminarEstudiante(ventanaEliminarEstudiante,entryCarnet.get()))
    botonEliminarEstudiante.config(width = "25",fg="black",font= ("Arial", 12))
    botonEliminarEstudiante.pack(padx=30, pady=20)

def abrirVentanaConfirmacionEliminarEstudiante(ventanaEliminarEstudiante,carnet):
    """
    Funcionalidad: Al ingresar el carnet y presionar el boton de buscar estudiante 
    se habre una ventana para verificar la confirmación 
    Entradas: Carnet (str) del estudiante a eliminar 
    Salidas: Na
    """
    ventanaConfirmacion = crearVentana("")
    dimensionarVentana(ventanaConfirmacion, 350, 200)
    labelConfirmacion = Label(ventanaConfirmacion, text="¿Desea confirmar la eliminación?")
    labelConfirmacion.pack(padx=20, pady=10)
    labelConfirmacion.config(font=('Helvatical bold', 12), bg = '#6fabaa')
    botonEliminar = Button(ventanaConfirmacion,text="Sí", )
    botonEliminar.config(width = "10",fg="black",font= ("Arial", 12))
    botonEliminar.pack(padx=10, pady=20)
    botonNoEliminar = Button(ventanaConfirmacion,text="No", command=lambda:abrirVentanaNoConfirmar(ventanaConfirmacion))
    botonNoEliminar.config(width = "10",fg="black",font= ("Arial", 12))
    botonNoEliminar.pack(padx=30, pady=20)
    ventanaConfirmacion.mainloop()    

#   ------------------------------------------------- VENTANAS DE REPORTES  -------------------------------------------------
def abrirVentanaReportes():
    """
    Funcionalidad: Al presionar el botón de reportes en la ventana principal, se crea una ventana que contiene
    los botones para generar reportes según la especificación
    Entradas: Na
    Salidas: Na
    """ 
    ventanaReportes = crearVentanaSecundaria("Reportes")
    dimensionarVentana(ventanaReportes, 350, 320)
    colocarBotonesVentanaReportes(ventanaReportes)
    ventanaReportes.mainloop()
def colocarBotonesVentanaReportes(ventanaReportes):
    """
    Funcionalidad: Coloca los botones en la ventana de reportes 
    Entradas: VentanaReportes 
    Salidas:Na
    """
    botonProvincia = Button(ventanaReportes,text="Por grupo", command=abrirVentanaReportesProvincia)
    botonProvincia.config(width = "25",fg="black",font= ("Arial", 12),bg='white')
    botonProvincia.pack(padx=30, pady=10)

    botonCliente = Button(ventanaReportes,text="Por Cliente", command=abrirVentanaReporteCliente)
    botonCliente.config(width = "25",fg="black",font= ("Arial", 12),bg='white')
    botonCliente.pack(padx=30, pady=10)

    botonCodigos = Button(ventanaReportes,text="Por Código", command=abrirVentanaReporteCodigos)
    botonCodigos.config(width = "25",fg="black",font= ("Arial", 12),bg='white')
    botonCodigos.pack(padx=30, pady=10)

    botonRegresar = Button(ventanaReportes,text="Regresar")
    botonRegresar.config(width = "25",fg="black",font= ("Arial", 12),bg='white', command=ventanaReportes.destroy)
    botonRegresar.pack(padx=30, pady=10)
##########################################   Reporte 1   #############################################
def abrirVentanaReportesProvincia():
    """
    Funcionalidad: Crea una ventana que contiene una caja de seleccion de los grupos existentes 
    Entradas: Na 
    Salidas:Ventana 
    """
    global Provincias
    try:
        ventanaReportesPorGrupo = crearVentana("Reportes por Provincia")
        dimensionarVentana(ventanaReportesPorGrupo, 350, 110)
        grupoSeleccionado = StringVar(ventanaReportesPorGrupo)
        grupoSeleccionado.set("Seleccione una Provincia")
        cajaSeleccionProvincia = OptionMenu(ventanaReportesPorGrupo, grupoSeleccionado, *grupos)
        cajaSeleccionProvincia.pack(padx=20, pady=10)
        #cajaSeleccionGrupo.pack(padx=20, pady=10)
        botonGenerar = Button(ventanaReportesPorGrupo,text="Generar", command=lambda:generarReportePorClientesProvincia(grupoSeleccionado.get()))
        botonGenerar.config(width = "25",fg="black",font= ("Arial", 12))
        botonGenerar.pack(padx=30, pady=10)
        ventanaReportesPorGrupo.mainloop()
    except: 
        mostrarLabelError()
def generarReportePorClientesProvincia(grupoSeleccionado):
    """
    Funcionalidad: Dado la provincia este genera el reporte HTML 
    Entradas: Provincia(str)
    Salidas: reporte html 
    """
    ventanaReportesProvincia = crearVentana("Reporte html por Categoría")
    dimensionarVentana(ventanaReportesProvincia, 350, 110)
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
def abrirVentanaReporteCliente():
    """
    Funcionalidad: Crea una ventana con la caja de seleccion para que se ingrese la categoria 
    de la que se quiere hacer el reporte
    Entradas: Na
    Salidas: ventana 
    """
    ventanaReporteCliente = crearVentana("Reportes por categoría de frase")
    dimensionarVentana(ventanaReporteCliente, 350, 110)
    entryCedula = Entry(ventanaReporteCliente, width=100, justify="center")
    entryCedula.config(font=('Helvatical bold', 10))
    entryCedula.pack(padx=30, pady=0)

    botonGenerar = Button(ventanaReporteCliente,text="Generar", command=lambda:generarReportePorCliente(entryCedula.get()))
    botonGenerar.config(width = "25",fg="black",font= ("Arial", 12))
    botonGenerar.pack(padx=30, pady=10)
    ventanaReporteCliente.mainloop()
def generarReportePorCliente(categoriaSeleccionada):
    """
    Funcionalidad: Dada la cedula se crea un html de cliente específico
    Entradas: categoria Seleccionada(str)
    Salidas: reporte html 
    """
    ventanaReporteCliente = crearVentana("Reporte html por Categoría")
    dimensionarVentana(ventanaReporteCliente, 420, 110)
    if validarCedula(categoriaSeleccionada):
        # Función que genere html de cliente especifico meterla en esta linea
        labelInforme = Label(ventanaReporteCliente, text=f"Se ha creado el reporte de:\n{categoriaSeleccionada}")
        labelInforme.pack(padx=20, pady=30)
        labelInforme.config(font=('Helvatical bold', 13), bg = '#153a7aa')
    else: 
        labelInforme = Label(ventanaReporteCliente, text="Error, cedula con formato incorrecto.")
        labelInforme.pack(padx=20, pady=30)
        labelInforme.config(font=('Helvatical bold', 13), bg = '#153a7a')
##########################################   Reporte 3    #############################################
def abrirVentanaReporteCodigos():
    """
    Funcionalidad: Crea una ventana 
    Entradas: Na
    Salidas: ventana 
    """
    ventanaReporteCodigo = crearVentana("Reportes por código")
    dimensionarVentana(ventanaReporteCodigo, 350, 110)
    entryCodigo = Entry(ventanaReporteCodigo, width=100, justify="center")
    entryCodigo.config(font=('Helvatical bold', 10))
    entryCodigo.pack(padx=30, pady=0)

    botonGenerar = Button(ventanaReporteCodigo,text="Generar", command=lambda:generarReporteCodigos(entryCodigo.get()))
    botonGenerar.config(width = "25",fg="black",font= ("Arial", 12))
    botonGenerar.pack(padx=30, pady=10)
    ventanaReporteCodigo.mainloop()
def generarReporteCodigos(categoriaSeleccionada):
    """
    Funcionalidad: Dado el codigo postal se crea un html de clientes
    Entradas: Codigo Seleccionada(str)
    Salidas: reporte html 
    """
    ventanaReporteCliente = crearVentana("Reporte html por Categoría")
    dimensionarVentana(ventanaReporteCliente, 420, 110)
    if validarCodigoPostal(categoriaSeleccionada):
        # Función que genere html de cliente especifico meterla en esta linea
        labelInforme = Label(ventanaReporteCliente, text=f"Se ha creado el reporte del código:\n{categoriaSeleccionada}")
        labelInforme.pack(padx=20, pady=30)
        labelInforme.config(font=('Helvatical bold', 13), bg = '#153a7aa')
    else: 
        labelInforme = Label(ventanaReporteCliente, text="Error, código con formato incorrecto.\nO código no existente")
        labelInforme.pack(padx=20, pady=30)
        labelInforme.config(font=('Helvatical bold', 13), bg = '#153a7a')
#def abrirVentanaReportesPorCategoriaFrase():
#    """
#    Funcionalidad: Crea una ventana que contiene cajas de selección para ingresar la categoría 
#    y en base a ello, la frase que se quiere para generar el reporte.
#    Entradas: Na 
#    Salidas: ventana 
#    """
#    ventanaReportesFrase = crearVentana("Reportes por categoría y frase")
#    dimensionarVentana(ventanaReportesFrase, 350, 160)
#    categorias = []
#    for frase in frases:
#        categorias.append(frase[0])
#    categoriaSeleccionada = StringVar(ventanaReportesFrase)
#    categoriaSeleccionada.set("Seleccione una categoría")
#
#    fraseSeleccionada = StringVar(ventanaReportesFrase)
#    fraseSeleccionada.set("Seleccione una frase")
#    cajaSeleccionFrases = OptionMenu(ventanaReportesFrase, fraseSeleccionada, *frasesMostradas)
#    cajaSeleccionCategoria = OptionMenu(ventanaReportesFrase, categoriaSeleccionada, *categorias, 
#    command=lambda categoriaSeleccionada: actualizarFrasesMostrar(categoriaSeleccionada, cajaSeleccionFrases, fraseSeleccionada))
#    cajaSeleccionCategoria.pack(padx=20, pady=10)
#    cajaSeleccionFrases.pack(padx=20, pady=10)
#
#    botonGenerar = Button(ventanaReportesFrase,text="Generar", command=lambda:generarReportePorCategoriaFrase(categoriaSeleccionada.get(), fraseSeleccionada.get()))
#    botonGenerar.config(width = "25",fg="black",font= ("Arial", 12))
#    botonGenerar.pack(padx=30, pady=10)

#def generarReportePorCategoriaFrase(categoriaSeleccionada, fraseSeleccionada):
#    """
#    Funcionalidad: Genera el reporte html de la frase 
#    Entradas: categoriaSeleccionada, fraseSeleccionada (str)
#    Salidas: Reporte html 
#    """
#    try:
#        ventanaReportesPorCategoriaFrase = crearVentana("Reporte html por Categoría")
#        dimensionarVentana(ventanaReportesPorCategoriaFrase, 400, 110)
#        if categoriaSeleccionada != "Seleccione una categoría": 
#            if fraseSeleccionada != "Seleccione una frase":
#                generarHtmlCategoriaFrase(categoriaSeleccionada, fraseSeleccionada)
#                labelInforme = Label(ventanaReportesPorCategoriaFrase, text=f"Se ha creado el reporte HTML de la frase: \n{fraseSeleccionada} ,con éxito.")
#                labelInforme.pack(padx=20, pady=30)
#                labelInforme.config(font=('Helvatical bold', 13), bg = '#6fabaa')
#            else: 
#                labelInforme = Label(ventanaReportesPorCategoriaFrase, text="Debe seleccionar una frase.")
#                labelInforme.pack(padx=20, pady=30)
#                labelInforme.config(font=('Helvatical bold', 13), bg = '#6fabaa')
#        else: 
#            labelInforme = Label(ventanaReportesPorCategoriaFrase, text="Debe seleccionar una categoría.")
#            labelInforme.pack(padx=20, pady=30)
#            labelInforme.config(font=('Helvatical bold', 13), bg = '#6fabaa')
#    except:
#        mostrarLabelError()
#

########################################### CREDENCIALES ##################################################
def abrirVentanaCredenciales():
    """
    Funcionalidad: Genera un las credenciales
    Entradas: Na 
    Salidas: N/A
    """
    ventanaCredencial = crearVentana("Reporte Excel")
    dimensionarVentana(ventanaCredencial, 350, 160)
    # Crear Función que muestre credenciales
    labelInforme = Label(ventanaCredencial, text="Las credenciales estan listas.")
    labelInforme.pack(padx=20, pady=30)
    labelInforme.config(font=('Helvatical bold', 13), bg = '#153a7a')

if __name__ == "__main__": #Si se ha ejecutado como programa principal se ejecuta el código dentro del condicional.
    iniciarInterfaz()


