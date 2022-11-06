from inventory_report.reports.colored_report import ColoredReport
from unittest.mock import patch

simple_report = (
    "Data de fabricação mais antiga: 20/07/2019\n"
    "Data de validade mais próxima: 06/05/2023\n"
    "Empresa com mais produtos: X Company"
)

expected_colored_report = (
    "\033[32mData de fabricação mais antiga:\033[0m 20/07/2019\n"
    "\033[32mData de validade mais próxima:\033[0m 06/05/2023\n"
    "\033[32mEmpresa com mais produtos:\033[0m \033[31mX Company\033[0m"
)


@patch("inventory_report.reports.simple_report.SimpleReport")
def test_decorar_relatorio(SimpleReport):
    SimpleReport.generate.return_value = simple_report
    colored_report = ColoredReport(SimpleReport)
    generated_report = colored_report.generate([])
    assert generated_report == expected_colored_report
