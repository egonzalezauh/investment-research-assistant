from fastapi import FastAPI
from pydantic import BaseModel

class Holding (BaseModel):
    fecha: str
    ticker: str
    open: float
    high:float 
    low: float
    close: float
    volume:int

app = FastAPI()

@app.get("/health")
def api_health():
    return {"status":"ok"}


@app.get("/holdings", response_model = list[Holding])
def get_holdings():
    fila1 = Holding(fecha="2026-09-25",ticker="AMD",open=550,high=660,low=530,close=630,volume=450045)
    fila2 = Holding(fecha="2026-09-25",ticker="GOOGL",open=200,high=300,low=196,close=240,volume=4345045)
    fila3 = Holding(fecha="2026-09-25",ticker="NOW",open=120,high=125,low=118,close=127,volume=23484)
    return [fila1,fila2,fila3]

@app.get("/ticker/{ticker}")
def get_ticker(ticker: str):
    return [f for f in get_holdings() if f.ticker == ticker]

