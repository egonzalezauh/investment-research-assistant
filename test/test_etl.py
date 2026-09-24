from semana1_python.main import leer_todo
import pytest

def test_leer_todo_devuelve_todas_las_filas():
    filas = leer_todo("data/precios_diarios.csv")
    assert len(filas) == 91680 


@pytest.fixture
def csv_pequeno(tmp_path):
    ruta = tmp_path / "mini.csv"
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        f.write("fecha,ticker,open,high,low,close,volume\n")   
        f.write("2024-01-02,AAPL,100,101,99,100.5,1000\n")
        f.write("2024-01-02,GOOG,200,202,198,201,1500\n")    
        f.write("2024-01-03,AAPL,101,102,100,101.5,1100\n")
        f.write("2024-01-03,GOOG,201,203,199,202,1600\n")
        f.write("2024-01-04,NOW,102,103,101,102.5,1200\n")
    return ruta
 

def test_leer_todo_con_csv_chiquito(csv_pequeno):
    filas = leer_todo(csv_pequeno)
    assert len(filas) == 5                      
    assert filas[0]["ticker"] == "AAPL" 
    assert all("fecha" in fila for fila in filas) and all("ticker" in fila for fila in filas) and all("open" in fila for fila in filas) and all("high" in fila for fila in filas) and all("low" in fila for fila in filas) and all("close" in fila for fila in filas) and all("volume" in fila for fila in filas)                   