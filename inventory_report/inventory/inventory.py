from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def read_xml(cls, path):
        with open(path) as file:
            content = xmltodict.parse(file.read())
        return content["dataset"]["record"]

    @classmethod
    def read_json(cls, path):
        with open(path) as file:
            content = file.read()
        return json.loads(content)

    @classmethod
    def read_csv(cls, path):
        with open(path) as file:
            content = list(csv.DictReader(file))
        return content

    @classmethod
    def read_file(cls, path):
        file_extension = path.split(".")[1]
        if file_extension == "csv":
            return cls.read_csv(path)
        elif file_extension == "json":
            return cls.read_json(path)
        elif file_extension == "xml":
            return cls.read_xml(path)

    @classmethod
    def import_data(cls, path, report_type):
        inventory = cls.read_file(path)

        if report_type == "simples":
            return SimpleReport.generate(inventory)
        elif report_type == "completo":
            return CompleteReport.generate(inventory)
