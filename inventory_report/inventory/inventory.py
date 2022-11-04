from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @classmethod
    def read_file(cls, path):
        with open(path) as file:
            content = file.read()
            return content

    @classmethod
    def read_csv(cls, path):
        with open(path) as file:
            content = csv.DictReader(file)
            return list(content)

    @classmethod
    def import_data(cls, path, report_type):
        inventory = cls.read_csv(path)
        if report_type == "simples":
            return SimpleReport.generate(inventory)
        elif report_type == "completo":
            return CompleteReport.generate(inventory)
