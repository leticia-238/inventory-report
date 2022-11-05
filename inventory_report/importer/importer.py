from abc import ABC, abstractmethod


class Importer(ABC):
    @classmethod
    def check_file_extension(cls, path, expected):
        file_extension = path.split(".")[1]
        if file_extension != expected:
            raise ValueError("Arquivo inválido")

    @classmethod
    @abstractmethod
    def import_data(cls, path):
        ...
