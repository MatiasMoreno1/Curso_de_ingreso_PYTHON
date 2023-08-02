import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:


A)  Al presionar el botón 'Agregar' se deberan cargar tantos vehiculos como el usuario desee. 
    Los datos a cargar de cada vehiculo son: marca (ford, volvo, fiat), tipo de vehiculo (auto, camioneta, moto) y kilometros*.

* Todos los autos son usados.

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar se deberan listar todos los vehiculos ingresados con su correspondiente kilometraje y su posicion en la lista.
Ejemplo: 1 - Ford - Auto - 1000 km
         2 - Fiat - Camioneta - 2000 km
         etc..

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) Al presionar el boton Informar 
    0- El mayor kilometraje y su tipo de vehiculo.
    1- El menor kilometraje y su tipo de vehiculo de marca 'Ford'.
    2- Kilometraje promedio de los autos por cada marca.
    3- Precio promedios de todos los servicios por marca.
    4- Informar los kilometrajes que superan el promedio (total) por tipo.
    5- Informar los kilometrajes que NO superan el promedio (total) por marca.
    6- Informar la cantidad de tipos por marca.
    7- Informar el precio promedio de los servicios cuyo kilometraje es mayor a 10000 kms de marca 'Volvo'.
    8- Indicar el mayor de los promedios de kilometros por tipo de vehiculo.
    9- Informar el monto promedio de los servicios de marca 'Ford'.


Los montos de los servicios son:
    - Auto: $15000
    - Camioneta: $25000
    - Moto: $10000
    
    *Si la marca es volvo tiene un recargo del 10%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("EXAMEN INGRESO")
        
        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_tipo_vehiculo = []
        self.lista_marca_vehiculo = []
        self.lista_kms_vehiculos = []

    def btn_agregar_on_click(self):
        contador = 0
        respuesta = True
        while respuesta :
            vehiculo = prompt("","Ingrese todos los vehiculos deseados\n Auto | Camioneta | Moto") 
            
            while vehiculo is None or vehiculo =="" or vehiculo.isdigit() and vehiculo != "Auto" and vehiculo!= "camioneta" and vehiculo != "moto" :
                vehiculo = prompt("","Vuelva a ingresar el tipo de vehiculo")
            self.lista_tipo_vehiculo.append(vehiculo) 
            marca = prompt("","Ingrese la marca \n ford, volvo, fiat")  
            while marca is None or marca == "" or marca.isdigit() and marca != "ford" and marca != "volvo" and marca != "fiat":
                marca=prompt("","vuelva a ingresar la marca")
            self.lista_marca_vehiculo.append(marca)
            kilometro = prompt("","Ingrese los kilometros")
            while kilometro is None or kilometro == "" or kilometro.isalpha():
                kilometro= prompt("","Vuelva a ingresar los kilometros")
            kilometro_int = int(kilometro)
            self.lista_kms_vehiculos.append(kilometro_int)   
            respuesta = question("","desea continuar?")      
        contador +=1
            
        print(respuesta)            
                

    
    def btn_mostrar_on_click(self):
        vehiculo = 0
        contador_vehiculo = 0
        for respuesta in (0,len(self.lista_tipo_vehiculo),0):
            vehiculo = self.lista_tipo_vehiculo[respuesta]
            kilometro = self.lista_kms_vehiculos[respuesta]
            mensaje = vehiculo + str(kilometro)
            print(mensaje)
            contador_vehiculo +=1

    def btn_informar_on_click(self):
        bandera = True
        acumulador_km = 0
        contador_vehiculos = 0
        for km in range(0,len(self.lista_kms_vehiculos),1):
            if bandera:
                if contador_vehiculos == acumulador_km:
                     pass
       
       
       
       
if __name__ == "__main__":
    app = App()
    app.geometry("200x400")
    app.mainloop()