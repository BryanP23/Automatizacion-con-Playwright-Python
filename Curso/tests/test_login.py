
from pages.login_page import LoginPage

def test_login_success(page, pytestconfig):
    base_url = pytestconfig.getini("demoqa_url")

    login_page = LoginPage(page)
    login_page.navigate(base_url)

    # Simular usuario válido
    login_page.login("usuario_demo", "password123")

    # Verificación: que aparezca un texto, url o elemento
    assert page.url.endswith("/dashboard") or page.is_visible("text=Bienvenido")
