import json

class Loader:
    @staticmethod
    def cargar(cls, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)

        # Si el archivo tiene una lista de instancias, se crean y se devuelven
        if isinstance(data, list):
            return [cls(**item) for item in data]
        else:  # Crear una sola instancia
            return cls(**data)
