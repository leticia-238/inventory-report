from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        cls.check_file_extension(path, "xml")

        with open(path) as file:
            content = xmltodict.parse(file.read())
        inventory = content["dataset"]["record"]
        return inventory
