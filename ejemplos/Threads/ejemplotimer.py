import threading
import time

# Evento que usaremos para bloquear al hilo "Esperador"
evento_inicio = threading.Event()

def tarea_programada():
    """Función que ejecuta el Timer tras la cuenta atrás."""
    print("\n⏰ [Temporizador]: ¡El tiempo ha terminado! Enviando la señal de inicio.")
    # El Timer ha expirado, ahora liberamos al hilo Esperador
    evento_inicio.set()

def hilo_esperador():
    """Hilo que espera a que el Timer expire y envíe la señal."""
    print("[Esperador] Esperando la señal del Timer...")
    evento_inicio.wait()
    print("[Esperador] ¡Señal recibida! Iniciando el trabajo principal.")

if __name__ == "__main__":
    # 1. Creamos el Timer: 5 segundos, ejecutará 'tarea_programada'
    t = threading.Timer(5.0, tarea_programada)
    
    # 2. Creamos el hilo Esperador
    h_esperador = threading.Thread(target=hilo_esperador)
    
    h_esperador.start()
    
    # 3. Iniciamos el Timer (comienza la cuenta atrás)
    print(f"[Main] Timer iniciado. La cuenta atrás durará {t.interval} segundos.")
    t.start()
    
    # Podemos hacer otras cosas mientras el Timer está corriendo
    time.sleep(1)
    print("[Main] El programa principal sigue trabajando mientras el Timer espera...")

    h_esperador.join()
    t.join() # Esperamos a que el Timer termine (aunque ya haya expirado)

    print("[Main] Programa finalizado.")