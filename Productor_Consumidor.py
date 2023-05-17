import time , random
import multiprocessing
import queue
def productor(cola):
    for i in range (10):
        producto_generado = f"producto {i}"
        cola.put(producto_generado)
        print(f"-P: producto {i} agregado")
        time.sleep(1)
        
        
def consumidor(cola):
    while True:
        producto_generado = cola.get()
        print(f"-C: {producto_generado} consumido")
        time.sleep(3)
        
    

