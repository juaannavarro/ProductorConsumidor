from prueba2 import *
if __name__ == '__main__':
    
    t1 = threading.Thread(target=productor)

    t2 = threading.Thread(target=consumidor)
    
    t1.start()

    t2.start()
    

    
