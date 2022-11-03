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


def test_cria_produto(product_info):
    product = Product(*product_info.values())
    assert product.id == product_info["id"]
    assert product.nome_do_produto == product_info["nome_do_produto"]
    assert product.nome_da_empresa == product_info["nome_da_empresa"]
    assert product.data_de_fabricacao == product_info["data_de_fabricacao"]
    assert product.data_de_validade == product_info["data_de_validade"]
    assert product.numero_de_serie == product_info["numero_de_serie"]
    assert (
        product.instrucoes_de_armazenamento
        == product_info["instrucoes_de_armazenamento"]
    )
