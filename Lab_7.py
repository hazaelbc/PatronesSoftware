# Importamos abc y abstractmethod del módulo abc
# abc es la clase base para definir clases abstractas,
# y abstractmethod permite marcar métodos que deben ser implementados en las subclases
from abc import ABC, abstractmethod

# Definimos una clase abstracta que actúa como plantilla para el algoritmo
class ClaseAbstracta(ABC):
    """
    ClaseAbstracta define el esqueleto del algoritmo en su método `metodo_plantilla`,
    permitiendo a las subclases implementar pasos específicos.
    """

    # Método plantilla que define la estructura general del algoritmo.
    # Este método controla el flujo de ejecución de los pasos y es final,
    # es decir, no se debe modificar por las subclases.
    def metodo_plantilla(self):
        self.paso_uno()  # Llamada al primer paso del algoritmo
        self.paso_dos()  # Llamada al segundo paso del algoritmo
        self.paso_tres()  # Llamada al tercer paso del algoritmo

    # Método abstracto que debe ser implementado por todas las subclases
    # Define el primer paso del algoritmo.
    @abstractmethod
    def paso_uno(self):
        pass
    
    # Método abstracto que debe ser implementado por todas las subclases
    # Define el segundo paso del algoritmo.
    @abstractmethod
    def paso_dos(self):
        pass

    # Método concreto que define un paso del algoritmo.
    # Las subclases pueden usar este método tal cual o sobrescribirlo si necesitan un
    # comportamiento diferente.
    def paso_tres(self):
        print("ClaseAbstracta: Paso Tres (Este paso puede ser opcional o común)")

# Clase concreta que implementa la clase abstracta
# Proporciona implementaciones específicas para paso_uno y paso_dos.
class ClaseConcretaA(ClaseAbstracta):
    """
    ClaseConcretaA implementa los pasos específicos del algoritmo según la estructura definida.
    """

    # Implementación del primer paso del algoritmo para ClaseConcretaA.
    def paso_uno(self):
        print("ClaseConcretaA: Paso Uno")

    # Implementación del segundo paso del algoritmo para ClaseConcretaA.
    def paso_dos(self):
        print("ClaseConcretaA: Paso Dos")

# Otra clase concreta que implementa la clase abstracta
# Proporciona implementaciones específicas para paso_uno y paso_dos,
# y también sobrescribe el método paso_tres.
class ClaseConcretaB(ClaseAbstracta):
    """
    ClaseConcretaB modifica un paso del algoritmo para su propia implementación.
    """

    # Implementación del primer paso del algoritmo para ClaseConcretaB.
    def paso_uno(self):
        print("ClaseConcretaB: Paso Uno")

    # Implementación del segundo paso del algoritmo para ClaseConcretaB.
    def paso_dos(self):
        print("ClaseConcretaB: Paso Dos")

    # Sobrescribimos el tercer paso del algoritmo con un comportamiento personalizado.
    def paso_tres(self):
        print("ClaseConcretaB: Paso Customizado Tres")

# Clase de prueba para validar el comportamiento de las clases concretas.
def test_patron_metodo_plantilla():
    """
    Clase de prueba que demuestra cómo el patrón Método Plantilla puede ser utilizado
    para definir un algoritmo general mientras permite que las subclases personalicen partes específicas.
    """

    # Creamos una instancia de ClaseConcretaA
    class_a = ClaseConcretaA()
    # Creamos una instancia de ClaseConcretaB
    class_b = ClaseConcretaB()

    # Ejecutamos el algoritmo definido en ClaseConcretaA
    print("Prueba con ClaseConcretaA:")
    class_a.metodo_plantilla()

    # Ejecutamos el algoritmo definido en ClaseConcretaB
    print("\nPrueba con ClaseConcretaB:")
    class_b.metodo_plantilla()

# Llamamos a la función de prueba si el script es ejecutado directamente
if __name__ == "__main__":
    test_patron_metodo_plantilla()
