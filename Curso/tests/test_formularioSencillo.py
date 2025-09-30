from pages.home_page import HomePage
from pages.formularioSencillo_page import FormularioSencilloPage
from playwright.sync_api import expect

def test_llenar_formulario(page, urls):
    # 🚀 Ir a la URL de DemoQA (desde pytest.ini)
    page.goto(urls["demoqa"])

    home = HomePage(page)
    home.go_to_formularioSencillo()

    FormularioSencillo = FormularioSencilloPage(page)
    FormularioSencillo.llenar_formulario(
        nombre="Bryan Polo", 
        email="Bryan.polo@example.com", 
        current_address="P sherman 53 sydney", 
        permanent_address="Perth Australia city"
    )
    
    FormularioSencillo.enviar_formulario()
    
 # ✅ Validación final: verificar que el output contenga lo enviado
    output = page.locator("#output")
    assert output.is_visible(), "❌ El formulario no mostró resultados"
    assert "Bryan Polo" in output.inner_text()
    assert "Bryan.polo@example.com" in output.inner_text()
    assert "P sherman 53 sydney" in output.inner_text()
    assert "Perth Australia city" in output.inner_text()
