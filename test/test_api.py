from fastapi.testclient import TestClient
from semana1_python.api import app

client = TestClient(app)

def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status":"ok"}
    
def test_holdings():                      # ← renombrada
    resp = client.get("/holdings")                # ← tú: la ruta de tu otra API
    assert resp.status_code == 200        # ← tú: ¿éxito es qué número?
    assert len(resp.json()) == 3        # ← tú: ¿cuántas filas retorna tu función?
    
def test_holdings_keys():                  
    resp = client.get("/holdings")               
    assert resp.status_code == 200       
    for fila in resp.json():
        assert set(fila.keys()) == {"fecha","ticker","open","high","low","close","volume"}
    
def test_ticker():
    resp = client.get("/ticker/AMD")
    assert resp.status_code == 200
    assert len(resp.json()) == 1
    assert resp.json()[0]["ticker"] == "AMD"
    
def test_ticker_not_found():
    resp = client.get("/ticker/META")
    assert resp.status_code == 200
    assert len(resp.json()) == 0
    
