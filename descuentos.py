#!/usr/bin/env python3
"""
Calculadora de Descuentos - Programa de línea de comandos
=========================================================

Este programa calcula el importe final después de aplicar un descuento porcentual
a un importe base. Está diseñado para ser ejecutado desde la línea de comandos
con dos argumentos: el importe base y el porcentaje de descuento.

Características:
    - Validación de entrada de datos
    - Manejo de errores robusto
    - Soporte para números decimales
    - Mensajes de error informativos

Uso:
    python descuentos.py <importe> <descuento>
    
Ejemplos:
    python descuentos.py 100 15        # Aplica 15% de descuento a 100
    python descuentos.py 99.99 12.5    # Aplica 12.5% de descuento a 99.99

Autor: Sistema de pruebas automatizado
Versión: 1.0
Fecha: 2025-06-20
"""

import sys


def calcular_descuento(importe, descuento):
    """
    Calcula el importe final después de aplicar un descuento porcentual.
    
    Esta función toma un importe base y un porcentaje de descuento, valida
    los datos de entrada y calcula el importe final después de aplicar el
    descuento correspondiente.
    
    Fórmula utilizada:
        importe_final = importe - (importe * descuento / 100)
    
    Args:
        importe (float): El importe base sobre el cual aplicar el descuento.
                        Debe ser un número no negativo.
        descuento (float): El porcentaje de descuento a aplicar.
                          Debe estar entre 0 y 100 (inclusive).
    
    Returns:
        float: El importe final después de aplicar el descuento.
               El resultado conserva la precisión decimal de los argumentos.
    
    Raises:
        ValueError: Si el importe es negativo.
        ValueError: Si el descuento es negativo.
        ValueError: Si el descuento es mayor al 100%.
    
    Examples:
        >>> calcular_descuento(100.0, 10.0)
        90.0
        >>> calcular_descuento(99.99, 15.0)
        84.99
        >>> calcular_descuento(100.0, 0.0)
        100.0
        >>> calcular_descuento(100.0, 100.0)
        0.0
    """
    # Validación de entrada: el importe debe ser un valor positivo o cero
    if importe < 0:
        raise ValueError("El importe no puede ser negativo")
    
    # Validación de entrada: el descuento no puede ser negativo
    if descuento < 0:
        raise ValueError("El descuento no puede ser negativo")
    
    # Validación de entrada: el descuento no puede exceder el 100%
    if descuento > 100:
        raise ValueError("El descuento no puede ser mayor al 100%")
    
    # Cálculo del importe del descuento: porcentaje aplicado al importe base
    importe_descuento = importe * (descuento / 100)
    
    # Cálculo del importe final: importe base menos el descuento calculado
    importe_final = importe - importe_descuento
    
    return importe_final


def main():
    """
    Función principal del programa - maneja la interfaz de línea de comandos.
    
    Esta función se encarga de:
    1. Validar que se proporcionen exactamente 2 argumentos
    2. Convertir los argumentos de string a float
    3. Llamar a la función calcular_descuento()
    4. Mostrar el resultado en stdout
    5. Manejar errores y mostrar mensajes informativos
    
    La función espera que sys.argv contenga exactamente 3 elementos:
    - sys.argv[0]: nombre del script (descuentos.py)
    - sys.argv[1]: importe base (string convertible a float)
    - sys.argv[2]: porcentaje de descuento (string convertible a float)
    
    Salida:
        El programa imprime el resultado en stdout como un número decimal.
        En caso de error, imprime mensajes informativos en stderr.
    
    Códigos de salida:
        0: Ejecución exitosa
        1: Error en argumentos o cálculo
    
    Examples:
        $ python descuentos.py 100 15
        85.0
        
        $ python descuentos.py 99.99 12.5
        87.49
        
        $ python descuentos.py 100
        Uso: python descuentos.py <importe> <descuento>
        Ejemplo: python descuentos.py 100 15
    """
    # Verificación de argumentos: debe haber exactamente 2 parámetros (importe y descuento)
    if len(sys.argv) != 3:
        print("Uso: python descuentos.py <importe> <descuento>", file=sys.stderr)
        print("Ejemplo: python descuentos.py 100 15", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Conversión de argumentos de string a float
        # sys.argv[1] = importe base, sys.argv[2] = porcentaje de descuento
        importe = float(sys.argv[1])
        descuento = float(sys.argv[2])
        
        # Llamada a la función principal de cálculo
        resultado = calcular_descuento(importe, descuento)
        
        # Salida del resultado: imprime solo el valor numérico
        print(f"{resultado}")
        
    except ValueError as e:
        # Manejo de errores: distingue entre errores de conversión y de validación
        if "could not convert" in str(e):
            # Error de conversión: los argumentos no son números válidos
            print("Error: Los argumentos deben ser números válidos", file=sys.stderr)
        else:
            # Error de validación: valores fuera de rango (negativo, >100%, etc.)
            print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    # Punto de entrada: ejecuta main() solo cuando el script se ejecuta directamente
    # (no cuando se importa como módulo)
    main()