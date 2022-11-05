from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        cls.check_file_extension(path, "csv")

        with open(path) as file:
            inventory = list(csv.DictReader(file))
        return inventory
