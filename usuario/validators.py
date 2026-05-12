import re
from django.core.exceptions import ValidationError

def validar_rut_chileno(rut):
    # 1. Limpieza básica (quitar puntos y guion)
    rut = rut.replace(".", "").replace("-", "").upper()
    
    # 2. Formato mínimo (7 u 8 dígitos + DV)
    if not re.match(r"^\d{7,8}[0-9K]$", rut):
        raise ValidationError("Formato de RUT inválido.")

    cuerpo = rut[:-1]
    dv_ingresado = rut[-1]

    # 3. Algoritmo Módulo 11
    reverso = map(int, reversed(cuerpo))
    factores = [2, 3, 4, 5, 6, 7, 2, 3] # Ciclo para RUTs de hasta 8 dígitos
    suma = sum(d * f for d, f in zip(reverso, factores))
    
    res = 11 - (suma % 11)
    
    if res == 11:
        dv_esperado = '0'
    elif res == 10:
        dv_esperado = 'K'
    else:
        dv_esperado = str(res)

    if dv_ingresado != dv_esperado:
        raise ValidationError("El dígito verificador del RUT no es correcto.")