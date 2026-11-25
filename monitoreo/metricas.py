
import psutil
import threading
import time

metricas = {
    "cpu": None,
    "ram": None,
    "temperatura": None
}

bloqueo = threading.Lock()
hilo = None


def obtener_temperatura():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as archivo:
            return float(archivo.read().strip()) / 1000
    except (OSError, ValueError):
        return None


def monitorear():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        temperatura = obtener_temperatura()

        with bloqueo:
            metricas["cpu"] = cpu
            metricas["ram"] = ram
            metricas["temperatura"] = temperatura

        time.sleep(2)


def iniciar_monitoreo():
    global hilo

    with bloqueo:
        if hilo is None or not hilo.is_alive():
            hilo = threading.Thread(
                target=monitorear,
                daemon=True
            )
            hilo.start()


def obtener_metricas():
    with bloqueo:
        return metricas.copy()

