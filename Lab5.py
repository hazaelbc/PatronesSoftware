import time

# Interfaz Command: Define la interfaz general para los comandos.
class Command:
    def execute(self):
        pass  # El método execute debe ser implementado por las subclases

# ConcreteCommand para encender la lámpara.
class EncenderLamparaCommand(Command):
    def __init__(self, lampara):
        self.lampara = lampara

    def execute(self):
        self.lampara.encender()

# ConcreteCommand para apagar la lámpara.
class ApagarLamparaCommand(Command):
    def __init__(self, lampara):
        self.lampara = lampara

    def execute(self):
        self.lampara.apagar()

# ConcreteCommand para preparar café en la cafetera.
class PrepararCafeCommand(Command):
    def __init__(self, cafetera):
        self.cafetera = cafetera

    def execute(self):
        self.cafetera.preparar_cafe()

# Receiver (Receptor) Lámpara con los métodos específicos.
class Lampara:
    def encender(self):
        print("La lámpara está encendida")

    def apagar(self):
        print("La lámpara está apagada")

# Receiver (Receptor) Cafetera con los métodos específicos.
class Cafetera:
    def preparar_cafe(self):
        print("El café está listo")

# Invoker (Invocador): Responsable de almacenar el comando y ejecutarlo.
class SistemaDomotico:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def ejecutar_comando(self):
        if self.command:
            self.command.execute()

# Cliente: Configura los comandos, receptores e invocador.
if __name__ == "__main__":
    # Crear los receptores
    lampara = Lampara()
    cafetera = Cafetera()

    # Crear comandos concretos
    comando_encender_lampara = EncenderLamparaCommand(lampara)
    comando_apagar_lampara = ApagarLamparaCommand(lampara)
    comando_preparar_cafe = PrepararCafeCommand(cafetera)

    # Crear el invocador (sistema domótico)
    sistema_domotico = SistemaDomotico()

    # Encender lámpara
    print("Encendiendo lámpara...")
    sistema_domotico.set_command(comando_encender_lampara)
    time.sleep(1)
    sistema_domotico.ejecutar_comando()

    # Apagar lámpara
    print("Apagando lámpara...")
    sistema_domotico.set_command(comando_apagar_lampara)
    time.sleep(1)
    sistema_domotico.ejecutar_comando()

    # Preparar café
    print("Preparando café...")
    sistema_domotico.set_command(comando_preparar_cafe)
    time.sleep(1)
    sistema_domotico.ejecutar_comando()

