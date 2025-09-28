import io
import contextlib
from unittest.mock import patch

try:
    from IrrAreas import InterfazPoligonoIrregular
except ImportError:
    print("Error: Asegúrate de que tu clase esté guardada en un archivo llamado 'IrrAreas.py'")
    exit()

def ejecutar_pruebas():
    """Función principal que ejecuta todas las pruebas."""
    print("--- Iniciando pruebas para la clase InterfazPoligonoIrregular ---")

    # --- PRUEBA 1: Cálculo de área correcto ---
    print("\n[Prueba 1: Cálculo de área de un cuadrado unitario]")
    try:
        # Vértices de un cuadrado de 1x1. El área esperada es 1.0.
        vertices_cuadrado = [(0, 0), (1, 0), (1, 1), (0, 1)]
        poligono_prueba = InterfazPoligonoIrregular(vertices_cuadrado)

        area_calculada = poligono_prueba.calcular_area()
        area_esperada = 1.0

        # Comprobar si el resultado es el correcto
        if area_calculada == area_esperada:
            print(f" ÉXITO: El área calculada ({area_calculada}) es igual a la esperada ({area_esperada}).")
        else:
            print(f" FALLO: El área calculada ({area_calculada}) NO es igual a la esperada ({area_esperada}).")

    except Exception as e:
        print(f" FALLO: La prueba generó un error inesperado: {e}")

    # --- PRUEBA 2: Error con menos de 3 vértices ---
    print("\n[Prueba 2: Creación de polígono inválido]")
    try:
        # Intentar crear un polígono con solo 2 vértices
        vertices_invalidos = [(0, 0), (1, 1)]
        _ = InterfazPoligonoIrregular(vertices_invalidos)

        # Si el código llega aquí, la prueba falló porque no se lanzó el error esperado.
        print(" FALLO: La clase NO lanzó un error al recibir menos de 3 vértices.")

    except ValueError as e:
        # Si se captura un ValueError, la prueba es exitosa.
        print(f" ÉXITO: La clase lanzó correctamente un error: '{e}'")
    except Exception as e:
        print(f" FALLO: Se lanzó un error diferente al esperado: {e}")


    # --- PRUEBA 3: Funcionamiento del menú interactivo ---
    print("\n[Prueba 3: Bucle y salida del menú principal]")
    try:
        # Simulamos una secuencia de entradas del usuario:
        # 1. '1': Elige la opción de crear un polígono.
        # 2. '0,0', '1,0', '1,1': Vértices del polígono.
        # 3. 'fin': Termina de añadir vértices.
        # 4. '2': Elige la opción de salir del menú.
        entradas_simuladas = ['1', '0,0', '1,0', '1,1', 'fin', '2']

        # Usamos 'patch' para reemplazar la función input() por nuestra lista de entradas.
        # 'side_effect' hace que en cada llamada a input() se retorne el siguiente elemento de la lista.
        with patch('builtins.input', side_effect=entradas_simuladas):
            # Capturamos todo lo que se imprima en la consola para verificarlo.
            f = io.StringIO()
            with contextlib.redirect_stdout(f):
                InterfazPoligonoIrregular.ejecutar() # Llamamos a la función que contiene el menú.
            salida_consola = f.getvalue() # Obtenemos el texto capturado.

        # Verificamos que el menú se mostró, se calculó el área y luego se salió.
        assert "--- Menú de Área de Polígono ---" in salida_consola
        assert "Resultado: El área del polígono es:" in salida_consola
        assert "Volviendo al menú principal..." in salida_consola
        # El menú debe aparecer 2 veces: una para la operación y otra antes de salir.
        assert salida_consola.count("--- Menú de Área de Polígono ---") == 2

        print(" ÉXITO: El menú se ejecutó, completó una operación, se volvió a mostrar y finalizó correctamente.")

    except Exception as e:
        print(f" FALLO: La prueba del menú generó un error inesperado: {e}")


    print("\n--- Pruebas finalizadas ---")


# Ejecutar las pruebas al correr el script
if __name__ == "__main__":
    ejecutar_pruebas()
    InterfazPoligonoIrregular.ejecutar()

