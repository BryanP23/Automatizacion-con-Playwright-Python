from pages.home_page import HomePage
from pages.check_Box_page import CheckBoxPage

def test_seleccionar_checkBox(page, urls):
   # 🚀 Ir a la URL de DemoQA (desde pytest.ini)
    page.goto(urls["demoqa"])
    
    home = HomePage(page)
    home.go_to_checkBox()

    CheckBox = CheckBoxPage(page)
    CheckBox.seleccionar_checkBox()
    
 # ✅ Validación final: verificar que el output contenga lo enviado
    output = page.locator(CheckBox.result)
    assert output.is_visible(), "❌ El checkbox no mostró resultados"
    assert "classified" in output.inner_text()
    