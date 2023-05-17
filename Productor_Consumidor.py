import time 
import multiprocessing
import queue
def productor(cola, semaforo_P, semaforo_C):
    for i in range (100):  # Producimos X productos
        producto_generado = f"producto {i}"
        semaforo_P.acquire() # Adquirimos el semaforo del productor
        cola.put(producto_generado) # Agregamos el producto a la cola
        print(f"-P: producto {i} agregado")
        semaforo_C.release() # Liberamos el semaforo del consumidor
        time.sleep(2)

        
        
        
        
def consumidor(cola, semaforo_P, semaforo_C):
    while True:
        semaforo_C.acquire() # Adquirimos el semaforo del consumidor
        producto_generado = cola.get() # Obtenemos el producto de la cola
        print(f"-C: {producto_generado} consumido") 
        semaforo_P.release() # Liberamos el semaforo del productor
        time.sleep(3)
        
    

