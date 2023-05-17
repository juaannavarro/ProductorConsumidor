from Productor_Consumidor import *
if __name__ == "__main__":
    cola = multiprocessing.Queue(5) # Creamos una cola de 5 elementos
    
    # Creamos los semaforos
    semaforo_P = multiprocessing.Semaphore(5)   
    semaforo_C = multiprocessing.Semaphore(0)
    # Creamos los procesos
    Proceso_productor = multiprocessing.Process(target=productor, args=(cola, semaforo_P, semaforo_C))
    Proceso_consumidor = multiprocessing.Process(target=consumidor, args=(cola, semaforo_P, semaforo_C))
    # Iniciamos los procesos
    Proceso_productor.start()
    Proceso_consumidor.start()
    # Esperamos a que terminen los procesos
    Proceso_productor.join()
    Proceso_consumidor.join()

    

    
