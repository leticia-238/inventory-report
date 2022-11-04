from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, inventory):
        current_date = datetime.now().strftime("%Y-%m-%d")
        oldest_manufacturing_date = [
            product["data_de_fabricacao"] for product in inventory
        ]
        earliest_expiration_date = [
            product["data_de_validade"]
            for product in inventory
            if product["data_de_validade"] >= current_date
        ]
        companies = dict()
        for product in inventory:
            product_qtd = companies.setdefault(product["nome_da_empresa"], 0)
            companies[product["nome_da_empresa"]] = product_qtd + 1

        company_name = Counter(companies).most_common(1)[0]
        oldest_manufacturing_date.sort()
        earliest_expiration_date.sort()
        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date[0]}\n"
            f"Data de validade mais próxima: {earliest_expiration_date[0]}\n"
            f"Empresa com mais produtos: {company_name[0]}"
        )
