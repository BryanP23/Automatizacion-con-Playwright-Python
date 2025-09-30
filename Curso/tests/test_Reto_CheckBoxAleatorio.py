from pages.home_page import HomePage
from pages.Reto_CheckBoxAleatorio_page import RetoCheckBoxAleatorioPage


def test_seleccionar_checkBox(page, urls):
    # 🚀 Ir a la URL de datatables (desde pytest.ini)
    page.goto(urls["datatables"])

    home = HomePage(page)
    home.go_to_RetoCheckBox()
    
    retoCheckBox = RetoCheckBoxAleatorioPage(page)
    retoCheckBox.seleccionar_checkBoxAleatorio()
    