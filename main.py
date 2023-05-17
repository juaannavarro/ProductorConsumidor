from Productor_Consumidor import *
if __name__ == "__main__":
    cola = multiprocessing.Queue(5)
    
    semaforo_P = multiprocessing.Semaphore(5)
    semaforo_C = multiprocessing.Semaphore(0)
    
    Proceso_productor = multiprocessing.Process(target=productor, args=(cola, semaforo_P, semaforo_C))
    Proceso_consumidor = multiprocessing.Process(target=consumidor, args=(cola, semaforo_P, semaforo_C))
    
    Proceso_productor.start()
    Proceso_consumidor.start()
    
    Proceso_productor.join()
    Proceso_consumidor.join()

    

    
