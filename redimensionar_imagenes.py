#	SE DEBEN CREAR LAS CARPETAS IMAGENES
# 	EN IMAGENES COLOCAR LAS IMAGENES QUE SE VAN A CONVERTIR
#	LA ESTRUCTURA DEBE SER LA SIGUIENTE EN LA RAIZ DEBE ESTAR EL SCRIPT, CARPETA IMAGENES
# 
from PIL import Image
import os
RAIZ = os.path.join(os.getcwd(), os.listdir(os.getcwd())[0])
IMAGENES = os.path.join(RAIZ, "imagenes")
REDIMENSIONADAS = os.path.join(RAIZ, "redimensionadas")
TAMANO = 300
EXTENSION = 'jpg'

def redimensionar():
    contador = 1
    cmd = f"rm -rf {REDIMENSIONADAS}"
    os.system(cmd)
    cmd = f"mkdir {REDIMENSIONADAS}"
    os.system(cmd)
    for item in os.listdir(IMAGENES):
        url_imagen = os.path.join(IMAGENES, item)
        nombre = str(contador).zfill(4)
        url_nueva = os.path.join(
            RAIZ, f"redimensionadas/{nombre}_{TAMANO}x{TAMANO}.{EXTENSION}")
        cmd = f"convert {url_imagen} -flatten -density 72 -depth 8 -resize {TAMANO}x{TAMANO}  -quality 100 -units PixelsPerInch {url_nueva}"
        os.system(cmd)
        contador = contador + 1

redimensionar()
