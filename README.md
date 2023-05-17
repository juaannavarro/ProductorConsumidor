# Productor y Consumidor

Hay dos roles importantes en los modelos de productor y consumidor: el productor es responsable de generar datos y el consumidor es responsable de obtener estos datos para la próxima operación. Para ejemplificar el desarrollo de un programa para productores y consumidores, asumimos que el productor es el que genera los recursos que van a utilizar los consumidores, por lo tanto los consumidores necesitan un proceso de sincronización con el productor para saber cuando el momento de consumir ha llegado.

Para ello hemos creado un modelo productor, un modelo consumidor y una cola ya incluida en el main.


1.Productor:

```
def productor(cola, semaforo_P, semaforo_C):
    for i in range (100):
        producto_generado = f"producto {i}"
        semaforo_P.acquire()
        cola.put(producto_generado)
        print(f"-P: producto {i} agregado")
        semaforo_C.release()
        time.sleep(1)
      
 ```

