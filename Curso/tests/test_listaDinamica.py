from time import time
from pages.home_page import HomePage
from pages.listaDinamica_page import listaDinamica_page     

def test_listaDinamica(page, urls):
    # 🚀 Ir a la URL de Google (desde pytest.ini)
    page.goto(urls["google"])
    
    listaDinamica = listaDinamica_page(page)    
    listaDinamica.buscar_auto()
    
    # validar que la busqueda contenga este localizador"
    assert page.locator("xpath=(//span[@class='VuuXrf'][normalize-space()='Volkswagen Colombia'])[1]").is_visible()
    time.sleep(3)