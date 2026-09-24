"""
SEMANA 1 — completada. Este archivo demuestra 3 cosas que ya escribiste tú:

  1) leer_todo   -> carga TODO el CSV en memoria (lento, ~150 ms, ~50 MB en RAM)
  2) leer_filas  -> GENERADOR: entrega una fila a la vez (top_10 sale en ~0.2 ms)
  3) @log_time   -> DECORADOR: envuelve una función para medir su tiempo,
                    sin tocar el código de adentro de esa función.

DATO: data/precios_diarios.csv ~91.680 filas simuladas
      (30 tickers, 2015 a sep-2026). Columnas: fecha,ticker,open,high,low,close,volume
"""
import csv
import time


# ══════════════════════════════════════════════════════════════════
# EL DECORADOR
# ══════════════════════════════════════════════════════════════════
# log_time NO ejecuta nada por sí solo. Es una FÁBRICA de funciones
# envueltas: recibe una función y devuelve OTRA función nueva que:
#   - corre la original
#   - mide cuánto tardó
#   - devuelve exactamente el mismo resultado de siempre
#
# Escribir @log_time encima de def leer_todo...
# es solo la forma corta de escribir, debajo de todo:
#   leer_todo = log_time(leer_todo)
#   # "reemplaza mi función por su versión envuelta con cronómetro"
#
# Por eso log_time debe estar DEFINIDO ANTES de usarse:
# Python lee el archivo de arriba hacia abajo — primero define, después usa.

def log_time(funcion_original):

    def funcion_nueva(ruta):
        t0 = time.perf_counter()
        resultado = funcion_original(ruta)   # el trabajo real, intacto
        t1 = time.perf_counter()
        print(f"  [log_time] {funcion_original.__name__} tardó {(t1 - t0) * 1000:.1f} ms")
        return resultado

    return funcion_nueva


# ══════════════════════════════════════════════════════════════════
# VERSIÓN "CARGONA": todo a la memoria de una sola patada
# ══════════════════════════════════════════════════════════════════
@log_time
def leer_todo(ruta_archivo):
    with open(ruta_archivo, newline="", encoding="utf-8") as f:
        data = list(csv.DictReader(f))   # list() = "carga TODO ahora"
    return data
    # Al decorarla, leer_todo quedó REEMPLAZADA por funcion_nueva.
    # Cada vez que alguien la llame, sale el print [log_time] gratis.


# ══════════════════════════════════════════════════════════════════
# VERSIÓN GENERADOR: el grifo. Una fila viva en RAM a la vez.
# ══════════════════════════════════════════════════════════════════
def leer_filas(ruta_archivo):
    with open(ruta_archivo, newline="", encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            yield fila   # entrego UNA y me duermo aquí, con el archivo abierto


# NOTA para la sesión 3 (no la intentes aún, solo piénsala):
# ¿Qué pasarías si decoramos leer_filas con @log_time?
# Pistas: ¿cuánto tarda "crear" un generador?
#         ¿en qué momento se lee el archivo: al llamarlo o al consumirlo?


# ══════════════════════════════════════════════════════════════════
# PRUEBA: solo las 10 primeras, sin cargar el resto
# ══════════════════════════════════════════════════════════════════
def top_10(ruta_archivo):
    gen = leer_filas(ruta_archivo)
    filas = []
    for _ in range(10):
        filas.append(next(gen))   # cada next() abre el grifo una gota
    return filas


if __name__ == "__main__":
    DATA = "data/precios_diarios.csv"

    print("── DUELO: las mismas 10 filas, dos caminos ──\n")

    # Camino A: el generador (NO decorado: lee solo lo que se pide)
    t0 = time.perf_counter()
    primeras = top_10(DATA)
    t1 = time.perf_counter()
    print(f"  GENERADOR: 10 filas en {(t1 - t0) * 1000:.2f} ms")
    for fila in primeras:
        print("    ", fila["fecha"], fila["ticker"], fila["close"])

    # Camino B: la cargona (decorada — ojo con el orden de los prints:
    # el [log_time] sale ANTES del total de afuera, porque el decorador
    # mide desde adentro de la llamada y termina primero)
    print()
    t0 = time.perf_counter()
    primeras_cargadas = leer_todo(DATA)[:10]
    t1 = time.perf_counter()
    print(f"  CARGONA: 10 filas (habiendo leído 91.680) en {(t1 - t0) * 1000:.2f} ms")
    for fila in primeras_cargadas:
        print("    ", fila["fecha"], fila["ticker"], fila["close"])

    print("\n  -> Mismas 10 filas. ~1000x de diferencia. Eso es yield.")
