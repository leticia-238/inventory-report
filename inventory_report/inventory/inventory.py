from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @classmethod
    def read_json(cls, path):
        with open(path) as file:
            content = file.read()
            return json.loads(content)

    @classmethod
    def read_csv(cls, path):
        with open(path) as file:
            content = csv.DictReader(file)
            return list(content)

    @classmethod
    def import_data(cls, path, report_type):
        file_extension = path.split(".")[1]
        inventory = []
        if file_extension == "csv":
            inventory = cls.read_csv(path)
        elif file_extension == "json":
            inventory = cls.read_json(path)

        if report_type == "simples":
            return SimpleReport.generate(inventory)
        elif report_type == "completo":
            return CompleteReport.generate(inventory)
