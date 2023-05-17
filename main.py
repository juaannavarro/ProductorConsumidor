from Productor_Consumidor import *
if __name__ == "__main__":
    cola = multiprocessing.Queue(2)
    Proceso_productor = multiprocessing.Process(target=productor, args=(cola,))
    Proceso_consumidor = multiprocessing.Process(target=consumidor, args=(cola,))
    
    Proceso_productor.start()
    Proceso_consumidor.start()
    
    Proceso_productor.join()
    Proceso_consumidor.join()

    

    
