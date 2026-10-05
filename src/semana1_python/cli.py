import argparse
from semana1_python.main import leer_filas
from semana1_python.llm import preguntar_stream

def top_n(n, ruta_archivo):
    gen = leer_filas(ruta_archivo)
    filas = []
    for _ in range(n):
        filas.append(next(gen))   # cada next() abre el grifo una gota
    return filas

def main():
    parser = argparse.ArgumentParser(description="Summarize a CSV with an LLM")
    parser.add_argument("archivo", help="Path to the CSV file")
    args = parser.parse_args()
    ruta_archivo = args.archivo
    
    top_20 = top_n(20, ruta_archivo)
    lineas = [",".join(fila.values()) for fila in top_20]
    texto = "\n".join(lineas)

    prompt = f"""Resume estos datos de precios de acciones.
Es solo una muestra de las primeras 20 filas de un archivo con muchas más.
No saques conclusiones sobre el archivo completo.
{texto}
"""
    
    for pedazo in preguntar_stream(prompt):
        print(pedazo, end="", flush=True)
    print("------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()
    
    