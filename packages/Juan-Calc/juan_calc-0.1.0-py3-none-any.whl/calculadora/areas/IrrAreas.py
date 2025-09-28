from typing import List, Tuple, Optional

class InterfazPoligonoIrregular:
    """
    Una interfaz para crear un polígono a partir de la entrada del usuario y calcular su área.
    Gestiona su propio menú de TUI (Interfaz de Usuario de Texto) para la creación
    y para volver al menú principal.
    """
    def __init__(self, vertices: List[Tuple[float, float]]):
        if len(vertices) < 3:
            raise ValueError("Un polígono debe tener al menos 3 vértices.")
        self.vertices = vertices
        self.n = len(vertices)

    def calcular_area(self) -> float:
        """Calcula el área usando la fórmula de la Lazada."""
        suma1 = sum(
            self.vertices[i][0] * self.vertices[(i + 1) % self.n][1]
            for i in range(self.n)
        )
        suma2 = sum(
            self.vertices[i][1] * self.vertices[(i + 1) % self.n][0]
            for i in range(self.n)
        )
        return 0.5 * abs(suma1 - suma2)

    @classmethod
    def desde_entrada_usuario(cls) -> Optional['InterfazPoligonoIrregular']:
        """
        Un método de clase que actúa como un constructor alternativo.
        Solicita los vértices al usuario y devuelve una nueva instancia de la clase.
        Devuelve None si el usuario decide no crear un polígono.
        """
        print("\n--- Crear Nuevo Polígono ---")
        print("Ingresa cada vértice como 'x,y'. Escribe 'fin' o presiona Enter para terminar.")

        vertices: List[Tuple[float, float]] = []
        while True:
            prompt = f"Vértice {len(vertices) + 1}: "
            entrada_usuario = input(prompt).strip()

            if not entrada_usuario or entrada_usuario.lower() == 'fin':
                if len(vertices) < 3:
                    print("Error: Se requieren al menos 3 vértices. No se creó el polígono.")
                    return None  # No se pudo crear un polígono válido
                else:
                    break # Vértices recopilados con éxito

            try:
                partes = entrada_usuario.split(',')
                if len(partes) != 2:
                    raise ValueError("Formato no válido.")
                x, y = float(partes[0]), float(partes[1])
                vertices.append((x, y))
            except ValueError:
                print("Entrada no válida. Por favor, ingresa las coordenadas como 'x,y'.")

        print(f"Se ha creado exitosamente un polígono con {len(vertices)} vértices.")
        return cls(vertices)

    @staticmethod
    def ejecutar():
        """
        Ejecuta el bucle del menú interactivo principal para la herramienta de polígonos.
        Este es el punto de entrada para este submódulo.
        """
        while True:
            print("\n--- Menú de Área de Polígono ---")
            print("1. Crear nuevo polígono y calcular área")
            print("0. Volver al menú principal")
            eleccion = input("Selecciona una opción: ").strip()

            if eleccion == '1':
                instancia_poligono = InterfazPoligonoIrregular.desde_entrada_usuario()
                if instancia_poligono:
                    area = instancia_poligono.calcular_area()
                    print(f"\n Resultado: El área del polígono es: {area:.4f}")
            elif eleccion == '0':
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción no válida, por favor selecciona 1 o 2.")
