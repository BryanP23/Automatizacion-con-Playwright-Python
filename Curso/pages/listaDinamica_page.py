class listaDinamica_page:
    def __init__(self, page):
        self.page = page
        self.search_input = "id=APjFqb"  # input de búsqueda de Google
        self.sugerencias_list = "//div[@class='erkvQe']"  # lista de sugerencias

    def buscar_auto(self):

        self.page.fill(self.search_input, "volkswagen jetta gli")  # escribir en el input
        # Esperar que aparezcan las sugerencias
        self.page.wait_for_selector(self.sugerencias_list)
        # Buscar entre las sugerencias alguna que contenga "2025"
        items = self.page.locator(self.sugerencias_list)
        count = items.count()
        
        for i in range(count):
            texto = items.nth(i).inner_text()
            if "2025" in texto:
                items.nth(i).click()
                return True  # se encontró y clickeó

        # Si ninguna sugerencia contiene "2025", falla la prueba
        raise AssertionError("❌ No se encontró ninguna sugerencia con '2025'")
    
    