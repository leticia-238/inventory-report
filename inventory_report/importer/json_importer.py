from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        cls.check_file_extension(path, "json")

        with open(path) as file:
            content = file.read()
        inventory = json.loads(content)
        return inventory
