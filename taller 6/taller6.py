from abc import ABC, abstractmethod

# Componente
class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass

# Hoja
class File(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def show_details(self):
        return f"File: {self.name} - Size: {self.size}MB"

# Composición (Contenedor)
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    def show_details(self):
        details = [f"Folder: {self.name}"]
        for component in self.components:
            details.append(f"  - {component.show_details()}")
        return "\n".join(details)

# Ejemplo de uso
file1 = File("file1.txt", 2)
file2 = File("file2.txt", 4)
folder = Folder("Documents")
folder.add_component(file1)
folder.add_component(file2)

print(folder.show_details())
