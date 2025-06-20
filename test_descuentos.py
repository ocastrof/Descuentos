"""
Suite de Pruebas Unitarias para el Programa de Descuentos
========================================================

Este módulo contiene todas las pruebas unitarias para validar el correcto
funcionamiento del programa descuentos.py. Incluye pruebas para casos
normales, casos límite, manejo de errores y generación de informes.

Características del sistema de pruebas:
    - Cobertura completa de funcionalidades
    - Pruebas de casos límite y manejo de errores
    - Generación automática de informes de resultados
    - Informes con timestamp para evitar sobrescritura
    - Validación de la interfaz de línea de comandos

Clases principales:
    - TestResult: Maneja la generación de informes de pruebas
    - TestDescuentos: Contiene todas las pruebas unitarias

Uso:
    python test_descuentos.py
    
El sistema genera automáticamente un informe en formato txt con:
    - Resumen de resultados (total, exitosas, fallidas)
    - Detalle de cada prueba con estado (PASS/FAIL)
    - Duración de ejecución
    - Timestamp de creación

Autor: Sistema de pruebas automatizado
Versión: 1.0
Fecha: 2025-06-20
"""

import unittest
import sys
import os
from unittest.mock import patch
from io import StringIO
from datetime import datetime

# Configuración del path para importar el módulo bajo prueba
# Añade el directorio actual al path de Python para permitir importar descuentos.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    # Intenta importar las funciones del módulo principal
    from descuentos import calcular_descuento, main
except ImportError:
    # Funciones stub en caso de que el módulo no esté disponible
    # Estas funciones vacías permiten que las pruebas se ejecuten sin errores
    # incluso si descuentos.py no existe o tiene errores de sintaxis
    def calcular_descuento(importe, descuento):
        """Función stub para calcular_descuento cuando no se puede importar"""
        pass
    
    def main():
        """Función stub para main cuando no se puede importar"""
        pass


class TestResult:
    """
    Clase para manejar la recolección y generación de informes de pruebas.
    
    Esta clase se encarga de:
    - Recopilar los resultados de todas las pruebas ejecutadas
    - Registrar tiempos de inicio y fin de ejecución
    - Generar informes detallados en formato de texto
    - Crear archivos con timestamp para evitar sobrescritura
    
    Attributes:
        test_results (list): Lista de diccionarios con resultados de pruebas
        start_time (datetime): Momento de inicio de las pruebas
        end_time (datetime): Momento de finalización de las pruebas
    """
    
    def __init__(self):
        """
        Inicializa una nueva instancia de TestResult.
        
        Configura las estructuras de datos necesarias para almacenar
        los resultados de las pruebas y los timestamps de ejecución.
        """
        # Lista para almacenar los resultados de cada prueba individual
        self.test_results = []
        # Timestamps para calcular la duración total de las pruebas
        self.start_time = None
        self.end_time = None
    
    def add_result(self, test_name, status, error_msg=None):
        """
        Agrega un resultado de prueba a la colección.
        
        Args:
            test_name (str): Nombre de la prueba ejecutada
            status (str): Estado de la prueba ('PASS' o 'FAIL')
            error_msg (str, optional): Mensaje de error si la prueba falló
        """
        # Crea un diccionario con la información de la prueba y lo añade a la lista
        self.test_results.append({
            'test_name': test_name,
            'status': status,
            'error_msg': error_msg
        })
    
    def generate_report(self, filename='informe_pruebas.txt'):
        """
        Genera un informe detallado de los resultados de las pruebas.
        
        Crea un archivo de texto con formato legible que incluye:
        - Encabezado con información del programa
        - Fecha y duración de ejecución
        - Resumen estadístico de resultados
        - Detalle de cada prueba con su estado
        - Conclusión final
        
        El archivo se genera con timestamp en el nombre para evitar
        sobrescribir informes anteriores.
        
        Args:
            filename (str): Nombre base del archivo (se añade timestamp)
            
        Note:
            El archivo generado usa codificación UTF-8 para soportar
            caracteres especiales como ✓ y ✗.
        """
        # Cálculo de estadísticas básicas del informe
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result['status'] == 'PASS')
        failed_tests = total_tests - passed_tests
        
        # Generar nombre de archivo con timestamp para evitar sobrescritura
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename_with_date = f"informe_pruebas_{timestamp}.txt"
        
        # Crear y escribir el archivo de informe con codificación UTF-8
        with open(filename_with_date, 'w', encoding='utf-8') as f:
            # Escribir encabezado del informe
            f.write("="*60 + "\n")
            f.write("INFORME DE PRUEBAS UNITARIAS - PROGRAMA DESCUENTOS\n")
            f.write("="*60 + "\n")
            f.write(f"Fecha de creación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Duración: {(self.end_time - self.start_time).total_seconds():.3f} segundos\n")
            f.write("\n")
            
            # Escribir sección de resumen estadístico
            f.write("RESUMEN DE RESULTADOS:\n")
            f.write("-" * 30 + "\n")
            f.write(f"Total de pruebas: {total_tests}\n")
            f.write(f"Pruebas exitosas: {passed_tests}\n")
            f.write(f"Pruebas fallidas: {failed_tests}\n")
            f.write(f"Porcentaje de éxito: {(passed_tests/total_tests)*100:.1f}%\n")
            f.write("\n")
            
            # Escribir sección de detalle de cada prueba
            f.write("DETALLE DE PRUEBAS:\n")
            f.write("-" * 30 + "\n")
            
            # Iterar sobre cada resultado y escribir su estado
            for i, result in enumerate(self.test_results, 1):
                # Símbolo visual para indicar éxito (✓) o fallo (✗)
                status_symbol = "✓" if result['status'] == 'PASS' else "✗"
                f.write(f"{i:2d}. [{status_symbol}] {result['test_name']} - {result['status']}\n")
                # Si hay mensaje de error, incluirlo en el informe
                if result['error_msg']:
                    f.write(f"     Error: {result['error_msg']}\n")
                f.write("\n")
            
            # Escribir conclusión final del informe
            f.write("="*60 + "\n")
            if failed_tests == 0:
                f.write("RESULTADO FINAL: TODAS LAS PRUEBAS PASARON CORRECTAMENTE\n")
            else:
                f.write(f"RESULTADO FINAL: {failed_tests} PRUEBA(S) FALLARON\n")
            f.write("="*60 + "\n")


# Instancia global del generador de informes para recolectar resultados de todas las pruebas
test_reporter = TestResult()


class TestDescuentos(unittest.TestCase):
    """
    Clase principal de pruebas unitarias para el programa descuentos.py.
    
    Esta clase hereda de unittest.TestCase y contiene todas las pruebas
    necesarias para validar el correcto funcionamiento del programa de
    cálculo de descuentos.
    
    Las pruebas cubren:
    - Cálculos básicos de descuentos
    - Casos límite (0%, 100%)
    - Manejo de números decimales
    - Validación de errores (valores negativos, descuentos > 100%)
    - Interfaz de línea de comandos
    - Manejo de argumentos inválidos
    
    Cada método de prueba registra automáticamente su resultado en el
    sistema de informes para generar reportes detallados.
    """
    
    def setUp(self):
        """
        Configuración ejecutada antes de cada prueba individual.
        
        Establece el nombre de la prueba actual para el sistema de informes
        y prepara cualquier configuración necesaria para la ejecución.
        """
        # Obtiene el nombre del método de prueba actual para el sistema de informes
        self.test_name = self._testMethodName
    
    def tearDown(self):
        """
        Limpieza ejecutada después de cada prueba individual.
        
        Actualmente no requiere limpieza específica, pero está disponible
        para futuras extensiones que requieran restaurar estado.
        """
        pass
    
    def test_descuento_basico(self):
        """
        Prueba el cálculo básico de descuento con valores estándar.
        
        Verifica que el cálculo de descuento funcione correctamente
        con valores típicos de uso (100 de base, 10% de descuento).
        
        Caso de prueba:
            Importe: 100.0
            Descuento: 10.0%
            Resultado esperado: 90.0
        """
        try:
            # Ejecutar el cálculo con valores de prueba estándar
            resultado = calcular_descuento(100.0, 10.0)
            # Verificar que el resultado sea el esperado
            self.assertEqual(resultado, 90.0)
            # Registrar éxito en el sistema de informes
            test_reporter.add_result(self.test_name, 'PASS')
        except Exception as e:
            # Registrar fallo en el sistema de informes y re-lanzar excepción
            test_reporter.add_result(self.test_name, 'FAIL', str(e))
            raise
    
    def test_descuento_cero(self):
        """Prueba con descuento 0%"""
        try:
            resultado = calcular_descuento(100.0, 0.0)
            self.assertEqual(resultado, 100.0)
            test_reporter.add_result(self.test_name, 'PASS')
        except Exception as e:
            test_reporter.add_result(self.test_name, 'FAIL', str(e))
            raise
    
    def test_descuento_completo(self):
        """Prueba con descuento 100%"""
        try:
            resultado = calcular_descuento(100.0, 100.0)
            self.assertEqual(resultado, 0.0)
            test_reporter.add_result(self.test_name, 'PASS')
        except Exception as e:
            test_reporter.add_result(self.test_name, 'FAIL', str(e))
            raise
    
    def test_importe_decimal(self):
        """Prueba con importes decimales"""
        try:
            resultado = calcular_descuento(99.99, 15.0)
            self.assertAlmostEqual(resultado, 84.99, places=2)
            test_reporter.add_result(self.test_name, 'PASS')
        except Exception as e:
            test_reporter.add_result(self.test_name, 'FAIL', str(e))
            raise
    
    def test_descuento_decimal(self):
        """Prueba con descuento decimal"""
        try:
            resultado = calcular_descuento(100.0, 12.5)
            self.assertEqual(resultado, 87.5)
            test_reporter.add_result(self.test_name, 'PASS')
        except Exception as e:
            test_reporter.add_result(self.test_name, 'FAIL', str(e))
            raise
    
    def test_valores_negativos_importe(self):
        """
        Prueba la validación de importes negativos.
        
        Verifica que la función rechace correctamente importes negativos
        lanzando una excepción ValueError con mensaje descriptivo.
        
        Caso de prueba:
            Importe: -100.0 (inválido)
            Descuento: 10.0%
            Resultado esperado: ValueError
        """
        try:
            # Verificar que se lance ValueError con importe negativo
            with self.assertRaises(ValueError):
                calcular_descuento(-100.0, 10.0)
            # Si llegamos aquí, la validación funcionó correctamente
            test_reporter.add_result(self.test_name, 'PASS')
        except Exception as e:
            # Error inesperado en la prueba
            test_reporter.add_result(self.test_name, 'FAIL', str(e))
            raise
    
    def test_valores_negativos_descuento(self):
        """Prueba que maneja descuentos negativos"""
        try:
            with self.assertRaises(ValueError):
                calcular_descuento(100.0, -10.0)
            test_reporter.add_result(self.test_name, 'PASS')
        except Exception as e:
            test_reporter.add_result(self.test_name, 'FAIL', str(e))
            raise
    
    def test_descuento_mayor_cien(self):
        """Prueba que maneja descuentos mayores al 100%"""
        try:
            with self.assertRaises(ValueError):
                calcular_descuento(100.0, 150.0)
            test_reporter.add_result(self.test_name, 'PASS')
        except Exception as e:
            test_reporter.add_result(self.test_name, 'FAIL', str(e))
            raise
    
    @patch('sys.argv', ['descuentos.py', '100', '10'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_argumentos_validos(self, mock_stdout):
        """
        Prueba la función main con argumentos válidos de línea de comandos.
        
        Verifica que la interfaz de línea de comandos funcione correctamente
        cuando se proporcionan argumentos válidos, usando mocks para simular
        sys.argv y capturar la salida.
        
        Caso de prueba:
            Argumentos simulados: ['descuentos.py', '100', '10']
            Resultado esperado: '90.0' en stdout
        """
        try:
            # Ejecutar la función main con argumentos simulados
            main()
            # Capturar la salida estándar del programa
            output = mock_stdout.getvalue()
            # Verificar que el resultado esperado esté en la salida
            self.assertIn("90.0", output)
            # Registrar éxito de la prueba
            test_reporter.add_result(self.test_name, 'PASS')
        except Exception as e:
            # Registrar fallo si algo sale mal
            test_reporter.add_result(self.test_name, 'FAIL', str(e))
            raise
    
    @patch('sys.argv', ['descuentos.py', '100'])
    @patch('sys.stderr', new_callable=StringIO)
    def test_main_argumentos_insuficientes(self, mock_stderr):
        """Prueba el main con argumentos insuficientes"""
        try:
            with self.assertRaises(SystemExit):
                main()
            test_reporter.add_result(self.test_name, 'PASS')
        except Exception as e:
            test_reporter.add_result(self.test_name, 'FAIL', str(e))
            raise
    
    @patch('sys.argv', ['descuentos.py', 'abc', '10'])
    @patch('sys.stderr', new_callable=StringIO)
    def test_main_argumentos_invalidos(self, mock_stderr):
        """Prueba el main con argumentos no numéricos"""
        try:
            with self.assertRaises(SystemExit):
                main()
            test_reporter.add_result(self.test_name, 'PASS')
        except Exception as e:
            test_reporter.add_result(self.test_name, 'FAIL', str(e))
            raise


if __name__ == '__main__':
    """
    Punto de entrada principal para la ejecución de pruebas.
    
    Este bloque se ejecuta cuando el archivo se ejecuta directamente
    (no cuando se importa como módulo). Configura el sistema de informes,
    ejecuta todas las pruebas y genera el informe final.
    
    Proceso:
    1. Registra el tiempo de inicio
    2. Ejecuta todas las pruebas con verbosidad alta
    3. Registra el tiempo de finalización
    4. Genera el informe de resultados
    5. Notifica al usuario sobre el archivo generado
    
    El informe se genera independientemente de si las pruebas
    pasan o fallan, garantizando siempre un registro completo.
    """
    # Registrar tiempo de inicio de las pruebas
    test_reporter.start_time = datetime.now()
    
    try:
        # Ejecutar todas las pruebas con alta verbosidad, sin salir al final
        unittest.main(verbosity=2, exit=False)
    finally:
        # Este bloque SIEMPRE se ejecuta, incluso si hay errores
        # Registrar tiempo de finalización
        test_reporter.end_time = datetime.now()
        # Generar el informe de resultados
        test_reporter.generate_report()
        # Mostrar mensaje informativo sobre el archivo generado
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename_with_date = f"informe_pruebas_{timestamp}.txt"
        print(f"\nInforme de pruebas generado: {filename_with_date}")