import time 
import multiprocessing
import queue
def productor(cola, semaforo_P, semaforo_C):
    for i in range (100):
        producto_generado = f"producto {i}"
        semaforo_P.acquire()
        cola.put(producto_generado)
        print(f"-P: producto {i} agregado")
        semaforo_C.release()
        time.sleep(1)

        
        
        
        
def consumidor(cola, semaforo_P, semaforo_C):
    while True:
        semaforo_C.acquire()
        producto_generado = cola.get()
        print(f"-C: {producto_generado} consumido")
        semaforo_P.release()
        time.sleep(4)
        
    

