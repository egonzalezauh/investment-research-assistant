"""
EJERCICIOS — sesión 3.5: tests sobre TU generador.

Mismo patrón de siempre: pytest corre las funciones test_* que empiezan
con "def test" y tienen asserts adentro.

Donde veas ... es un HUECO para ti: es un literal válido de Python
("Ellipsis") que hace que el test truene en rojo, en propósito.
Que salgan rojos primero es parte del ejercicio: vas a aprender a LEER
la salida de un fallo (igual de valioso que un verde).

Orden sugerido: 1 -> 2 -> 3 -> 4 (dificultad creciente).
Corre todos:  uv run pytest
Corre uno:    uv run pytest -k gota      (por ejemplo)
"""
import pytest
from semana1_python.main import leer_filas


# ═══════════════════════════════════════════════════════════════
# EL FIXTURE — te lo dejo YA HECHO para que veas que lo entendiste:
# mismo patrón que tu csv_pequeno, pero con otros datos.
# Léelo y comprueba que cada línea te resulta familiar.
# ═══════════════════════════════════════════════════════════════
@pytest.fixture
def mini_bursatil(tmp_path):
    ruta = tmp_path / "bolsa.csv"
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        f.write("fecha,ticker,open,high,low,close,volume\n")
        f.write("2024-03-01,ECOM,50,52,49,51,200\n")
        f.write("2024-03-04,ECOM,51,53,50,52,210\n")
        f.write("2024-03-05,BANCA,80,82,79,81,300\n")
    return ruta   # 3 filas de datos, no 5. Ojo con ese número.


# ═══════════════════════════════════════════════════════════════
# EJERCICIO 1 — el generador entrega dicts, como su hermana mayor
# Pista: leer_filas(ruta) devuelve un GENERADOR (el grifo), no una
# lista. Para contar todo lo que sale del grifo... hay que consumirlo.
# Ya viste la función que mete un iterable en lista completa.
# ═══════════════════════════════════════════════════════════════
def test_generador_entrega_las_3_filas(mini_bursatil):
    filas = list(leer_filas(mini_bursatil))               # convierte TODO el grifo en lista
    assert len(filas) == 3           # ¿cuántas filas de datos hay arriba?


# ═══════════════════════════════════════════════════════════════
# EJERCICIO 2 — next() funciona igual sobre tu generador
# Pista: crea el grifo, saca UNA gota, mírala.
# ¿Qué llave tiene la fila del medio? ¿Qué valor?
# isinstance(x, tipo) pregunta "¿x es de este tipo?" — los dicts son
# un builtin, su nombre va sin comillas y sin importarlo.
# ═══════════════════════════════════════════════════════════════
def test_primera_gota_del_grifo(mini_bursatil):
    grifo = leer_filas(mini_bursatil)
    primera = next(grifo)               # la primera fila, con next()
    assert primera["ticker"] == "ECOM"    # ¿qué ticker tenía la fila 1 del fixture?
    assert isinstance(primera, dict)    # ¿qué TIPO de objeto es?


# ═══════════════════════════════════════════════════════════════
# EJERCICIO 3 — cuando el grifo se seca, pasa algo EXPLÍCITO
# 3 filas + pedir la 4ª = el generador se rinde. ¿Con qué error?
# pytest tiene un "assert que espera que truene":
#   with pytest.raises(NombreDelError):
#       ...la línea que explota...
# ¿Qué error lanza un generador agotado? Corré el test en rojo y
# la propia salida de pytest te sopla la respuesta al oído. 😉
# (Pista extra: es un error BUILTIN, se escribe sin comillas e
#  importarlo — como cuando usaste ValueError en tu cabeza.)
# ═══════════════════════════════════════════════════════════════
def test_grifo_se_agota(mini_bursatil):
    grifo = leer_filas(mini_bursatil)
    for _ in range(3):
        next(grifo)                    # vacío el grifo: 3 gotas
    with pytest.raises(StopIteration):           # ¿qué excepción?
        next(grifo)                    # la gota 4... no existe


# ═══════════════════════════════════════════════════════════════
# EJERCICIO 4 (el boss) — leer TODO un CSV VACÍO no es un error
# Un CSV con solo el header tiene 0 filas de datos. ¿Tu código
# aguanta la borda, o truena? (spoiler de vida: los datos reales
# llegan vacíos MUCHO más seguido de lo que uno espera.)
# El primer ... te toca escribir TU PROPIO fixture (copy-paste del
# mini_bursatil y le recortas las 3 filas → solo header).
# ═══════════════════════════════════════════════════════════════
@pytest.fixture
def mini_vacio(tmp_path):
    ruta = tmp_path / "vacio.csv"
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        f.write("fecha,ticker,open,high,low,close,volume\n")                   # el header nada más... ¿recuerdas el \n?
    return ruta


def test_csv_vacio_devuelve_lista_vacia(mini_vacio):
    filas = list(leer_filas(mini_vacio))                        # consume TODO el grifo vacío → lista
    assert filas == []                # ¿cómo se ve "una lista sin nada"?
