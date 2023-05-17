# Productor y Consumidor

Hay dos roles importantes en los modelos de productor y consumidor: el productor es responsable de generar datos y el consumidor es responsable de obtener estos datos para la próxima operación. Para ejemplificar el desarrollo de un programa para productores y consumidores, asumimos que el productor es el que genera los recursos que van a utilizar los consumidores, por lo tanto los consumidores necesitan un proceso de sincronización con el productor para saber cuando el momento de consumir ha llegado.

Para ello hemos creado un modelo productor, un modelo consumidor y una cola ya incluida en el main.


1.Productor:

```
def productor(cola, semaforo_P, semaforo_C):
    for i in range (100):  # Producimos X productos
        producto_generado = f"producto {i}"
        semaforo_P.acquire() # Adquirimos el semaforo del productor
        cola.put(producto_generado) # Agregamos el producto a la cola
        print(f"-P: producto {i} agregado")
        semaforo_C.release() # Liberamos el semaforo del consumidor
        time.sleep(1)
      
 ```

2.Consumidor:

```
def consumidor(cola, semaforo_P, semaforo_C):
    while True:
        semaforo_C.acquire() # Adquirimos el semaforo del consumidor
        producto_generado = cola.get() # Obtenemos el producto de la cola
        print(f"-C: {producto_generado} consumido") 
        semaforo_P.release() # Liberamos el semaforo del productor
        time.sleep(2)
```

3.Main:
```
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
```

