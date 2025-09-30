import time
from playwright.sync_api import expect

class RetoCheckBoxAleatorioPage:
    def __init__(self, page):
        self.page = page
        self.checkbox ="xpath=//tbody/tr[1]/td[1]/input[1]"
    
    def seleccionar_checkBoxAleatorio(self):
        
        # for i in range(1, 11): # se seleccionan 1 por 1 todos los checkbox
        # #for i in range(1, 11, 2):   # recuerda el ultimo numero se utiliza para el incremento, en este caso de 2 en 2
        #     self.page.locator(f"xpath=//tbody/tr[{i}]/td[1]/input[1]").click()
            
        #     if i == 3:  # se detiene en el tercer checkbox
        #         self.page.locator(f"xpath=//button[normalize-space()='2']").click()
                
        #     if i == 6:  # se detiene en el sexto checkbox
        #         self.page.locator(f"xpath=//button[normalize-space()='3']").click()

        # Página 1
        for i in range(1, 11):
            self.page.locator(f"//tbody/tr[{i}]/td[1]/input[1]").click()

        # Página 2
        self.page.locator("//button[normalize-space()='2']").click()
        for x in range(1, 11, 2):  # Selecciona de 2 en 2
            self.page.locator(f"//tbody/tr[{x}]/td[1]/input[1]").click()

        # Página 3
        self.page.locator("//button[normalize-space()='3']").click()
        for y in range(1, 11):
            self.page.locator(f"//tbody/tr[{y}]/td[1]/input[1]").click()

        # --- Ahora el filtro fuera de los bucles ---
        self.page.locator("//input[@id='dt-search-0']").fill("je")

        # Esperar a que se apliquen los resultados
        self.page.wait_for_selector("//tbody/tr[4]/td[1]")

        # Seleccionar la fila 4 del resultado filtrado
        self.page.locator("//tbody/tr[4]/td[1]").click()
        time.sleep(2)
