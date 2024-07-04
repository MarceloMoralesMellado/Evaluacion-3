import os
import funciones
pedido = []
    
def menu():
    while True:
        print ("1.	Registrar pedido")
        print ("2.	Listar los todos los pedidos")
        print ("3.	Imprimir hoja de ruta")
        print ("4.	Buscar un pedido por ID")
        print ("5.	Salir del programa")
        opcion = input("ingresa una opcion")
        os.system()
    

        if opcion == "1":
             registro_pedido()

        elif opcion == "2":
             listar_pedido()

        elif opcion == "3":
             hoja_ruta()

        elif opcion == "4":
             buscar_pedido()

        elif opcion == "5":
             break
        
def id_pedido():
     id = random.randint(1000000.9999999)
            
def registro_pedido():   
        nombre = input("ingresa tu nombre")
        apellido = input("ingresa tu apellido")
        comuna = input("ingresa tu comuna")
        dispensador_6lts = int(input("cuantos de 6 lts necesitas"))
        dispensador_10lts = int(input("cuantos 10 lts necesitas"))
        dispensador_20lts = int(input("cuantos 20 lts necesitas"))

def listar_pedido():     

def hoja_ruta():
     
def buscar_pedido():
    

     
