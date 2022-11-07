import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def main():
    try:
        path = sys.argv[1]
        report_type = sys.argv[2]
    except IndexError:
        sys.stderr.write("Verifique os argumentos\n")
    else:
        importers = {
            "csv": CsvImporter,
            "json": JsonImporter,
            "xml": XmlImporter,
        }
        reports = {
            "simples": SimpleReport,
            "completo": CompleteReport,
        }

        file_extension = path.split(".")[1]
        inventory = InventoryRefactor(importers[file_extension])
        inventory.import_data(path, report_type)
        report = reports[report_type].generate(inventory.data)
        print(report, end="")


if __name__ == "__main__":
    main()
