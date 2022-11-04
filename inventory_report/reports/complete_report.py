from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, inventory):
        simple_report = super().generate(inventory)
        stock_by_company = cls.stock_by_company(inventory)
        formated = "".join(
            [
                f"- {company_name}: {product_qtd}\n"
                for company_name, product_qtd in stock_by_company.items()
            ]
        )
        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{formated}"
        )
