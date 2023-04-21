import queue , random

import threading 
import logging
import time
# Crear cola

#crear lista vacia con 10 elementos como maximo
cola = {}

def productor():
    global cola
    producto = 0
    while True:
        producto += 1
        cola[producto] = producto
        time.sleep(1)
        print("producto agregado")


            
        
        
def consumidor():
    global cola
    while True:
        if len(cola) > 0:
            print(cola.popitem())
            time.sleep(1)
            print("producto consumido")
        else:
            print("cola vacia")
            time.sleep(1)

            
        

        
        






