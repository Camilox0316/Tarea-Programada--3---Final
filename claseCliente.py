"""
Elaborador por:       
- Mario Barboza Artavia
- Camilo Sánchez Rodríguez
Fecha de creación:    10/11/2021, 00:17
Última edición:       31/10/2021, 10:40 XM
Versión:              Python 3.9.6
"""
##############################################################
#####              Definición de clases                  #####
##############################################################
import tkinter as tk
from tkinter import messagebox, ttk

class Cliente():
    def __init__(self):
        """
        Método constructor: crea la instancia para la clase Cliente
        Método que se llama al instanciar
        """
        self.cedula = ""
        self.nombre = ("", "", "")
        self.dirEspecifica = ""
        self.dirGeneral = ["", "", ""]
        self.codigoPostal = 0
        self.correo = ""
        return 

    def asignarCedula(self, pcedula):
        """
        Función: Asigna la cédula al cliente
        Entradas: 
        -pcedula(str): Es la cédula a asignar al cliente
        Salidas: N/A
        """
        self.cedula = pcedula
        return 

    def obtenerCedula(self):
        """
        Función: Obtiene la cedula de un objeto
        Entradas: N/A
        Salidas: Retorna Str(); es la cedula del cliente
        """
        return self.cedula

    def asignarNombre(self, pnombre):
        """
        Función: Asigna el nombre al cliente
        Entradas:
        -pnombre(tuple): Es el nombre a asignar al cliente; (nombre, apellido1, apellido2)
        Salidas: N/A
        """
        self.nombre = pnombre
        return
    
    def obtenerNombre(self):
        """
        Función: Obtiene el nombre del cliente
        Entradas: N/A
        Salidas: tuple(); es la tupla que contiene el nombre del cliente
        """
        return self.nombre
    
    def asignarDirEspecifica(self, pdirEspe):
        """
        Función: Asigna la direccion especifica de un cliente
        Entradas:
        -pdirEspe(str): Es la dirección específica del cliente
        Salidas: N/A
        """
        self.dirEspecifica = pdirEspe
        return 
    
    def obtenerDirEspecifica(self):
        """
        Función: Obtiene la dirección específica del cliente
        Entradas: N/A
        Salidas: Str(); es la direccion del cliente
        """
        return self.dirEspecifica
    
    def asignarDirGeneral(self, pdirGen):
        """
        Función: Asigna la direccion general a un cliente
        Entradas:
        -pdirGen(list): Es una lista de strings que contiene la dirección general del cliente
        Salidas: N/A
        """
        self.dirGeneral = pdirGen
        return 
    
    def obtenerDirGeneral(self):
        """
        Función: Obtiene la dirección general de un cliente
        Entradas: N/A
        Salidas: list(); retorna una lista que contiene la direccion general del cliente
        """
        return self.dirGeneral
    
    def asignarCodigoPostal(self, pcodigo):
        """
        Función:    Asigna el código postal del cliente
        Entradas:   
        pcodigo(int): es el código postal del cliente
        Salidas: N/A
        """
        self.codigoPostal = pcodigo
        return 
    
    def obtenerCodigoPostal(self):
        """
        Función: Obtiene el código postal del cliente
        Entradas: N/A
        Salidas: Int(); retorna el codigo postal del cliente
        """
        return self.codigoPostal
    
    def asignarCorreo(self, pcorreo):
        """
        Función: Asigna el correo a un cliente
        Entradas: 
        -pcorreo(str): es el correo del cliente
        Salidas: N/A
        """
        self.correo = pcorreo
        return 
    
    def obtenerCorreo(self):
        """
        Función: Obtiene el correo del cliente
        Entradas: N/A
        Salidas: Str(); es el correo del usuario
        """
        return self.correo
    def obtenerDatos(self):
        """
        Función: Obtiene los datos y los inserta en tupla
        Entradas: N/A
        Salidas: tuple(); datos
        """
        return (self.obtenerNombre(),self.obtenerDirEspecifica(),self.obtenerDirGeneral(),self.obtenerCodigoPostal(),
        self.obtenerCorreo())

    def obtenerCedNom(self):
        """
        Función: Obtiene los datos de  nombre y cédula
        Entradas: N/A
        Salidas: tuple(); datos
        """
        return (self.obtenerNombre(),self.obtenerCedula())
    def mostrarDatos(self): ##### Esta funcion es mantequilla, es para ver como guarda a los clientes XD #####
        print(f"\ncedula: {self.obtenerCedula()}\n"
        f"Nombre completo: {self.obtenerNombre()}\n"
        f"Dir espe: {self.obtenerDirEspecifica()}\n"
        f"Dir general: {self.obtenerDirGeneral()}\n"
        f"codigo postal: {self.obtenerCodigoPostal()}\n"
        f"correo: {self.obtenerCorreo()}\n"
        f"Demostración que es un objeto: {type(self)}")
        return ""
    
"""
clienteActual = Cliente()
clienteActual.asignarCedula("1-0000-0000")
clienteActual.asignarNombre(("camilo", "sánchez", "rodríguez"))
clienteActual.asignarDirEspecifica("Ca ## Av ## # ##")
clienteActual.asignarDirGeneral(["san jose", "san jose", "paso ancho"])
clienteActual.asignarCodigoPostal(10110)
clienteActual.asignarCorreo("camsanchez@gmail.com")
print(f"Cédula: {clienteActual.obtenerCedula()}")
print(f"Nombre: {clienteActual.obtenerNombre()}")
print(f"Dir espe: {clienteActual.obtenerDirEspecifica()}")
print(f"Dir gen: {clienteActual.obtenerDirGeneral()}")
print(f"code postal: {clienteActual.obtenerCodigoPostal()}")
print(f"Correo: {clienteActual.obtenerCorreo()}")
"""    