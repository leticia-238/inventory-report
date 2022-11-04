from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def stock_by_company(cls, inventory):
        companies = [p["nome_da_empresa"] for p in inventory]
        return Counter(companies)

    @classmethod
    def generate(cls, inventory):
        current_date = datetime.now().strftime("%Y-%m-%d")
        oldest_manufacturing_date = inventory[0]["data_de_fabricacao"]
        earliest_expiration_date = inventory[0]["data_de_validade"]

        for p in inventory:
            if p["data_de_fabricacao"] < oldest_manufacturing_date:
                oldest_manufacturing_date = p["data_de_fabricacao"]
            if (
                earliest_expiration_date
                > p["data_de_validade"]
                >= current_date
            ):
                earliest_expiration_date = p["data_de_validade"]

        company_name, _ = cls.stock_by_company(inventory).most_common(1)[0]

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {earliest_expiration_date}\n"
            f"Empresa com mais produtos: {company_name}"
        )
