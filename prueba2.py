import time , random
import threading
producto = 0

def productor():
    global producto
    while True:
        if producto == 0:
            producto_generado = random.randint(1,10)
            producto = producto + producto_generado
            print("producto agregado")
            time.sleep(3)
        else:
            print("cola llena")
            time.sleep(3)
            
def consumidor():
    global producto
    while True:
        if producto == 0:
            print("cola vacia")
            time.sleep(3)
        else:
            print("producto consumido")
            producto = producto - 1
            time.sleep(3)
  
            
            
            
