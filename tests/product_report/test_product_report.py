from inventory_report.inventory.product import Product
import pytest


@pytest.fixture
def product_info():
    return {
        "id": "1",
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2021-02-18",
        "data_de_validade": "2023-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1",
    }


def test_relatorio_produto(product_info):
    product = Product(**product_info)
    assert product.__repr__() == (
        "O produto Nicotine Polacrilex"
        " fabricado em 2021-02-18"
        " por Target Corporation"
        " com validade até 2023-09-17"
        " precisa ser armazenado instrucao 1."
    )
