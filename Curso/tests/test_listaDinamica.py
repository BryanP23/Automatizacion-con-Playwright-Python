from time import time
from pages.listaDinamica_page import listaDinamica_page     

def test_listaDinamica(page, urls):
    # 🚀 Ir a la URL de Google (desde pytest.ini)
    page.goto(urls["google"])
    
    listaDinamica = listaDinamica_page(page)    
    listaDinamica.buscar_auto()
    
    # Validar que en los resultados aparezca "Volkswagen 2025"
    assert page.locator("text=2025").is_visible()
        