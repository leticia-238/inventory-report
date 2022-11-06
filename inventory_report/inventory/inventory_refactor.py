from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.__importer = importer
        self.__data = []

    @property
    def importer(self):
        return self.__importer

    @importer.setter
    def importer(self, importer):
        self.__importer = importer

    @property
    def data(self):
        return self.__data

    def import_data(self, path, _):
        self.__data += self.__importer.import_data(path)

    def __iter__(self):
        return InventoryIterator(self.__data)
