import time
from playwright.sync_api import expect

class FormularioSencilloPage:
    def __init__(self, page):

        # Establecer un tiempo de espera predeterminado
        #page.set_default_timeout(5000)
        self.page = page
        self.name_input = "id=userName"
        self.email_input = "id=userEmail"
        self.current_address = "//textarea[@id='currentAddress']"
        self.permanent_address = "//textarea[@id='permanentAddress']"
        self.submit_button = "id=submit"
        
    def llenar_formulario(self, nombre, email, current_address, permanent_address):
        
        # Esperar que esté visible antes de llenar
        expect(self.page.locator(self.name_input)).to_be_visible()  # Esperar a que el campo de nombre sea visible
        self.page.fill(self.name_input, nombre)
        expect(self.page.locator(self.email_input)).to_be_visible()  # Esperar a que el campo de email sea visible
        self.page.fill(self.email_input, email)

        # Tiempo Forzado Antes de llenar las direcciones
        time.sleep(2)
        self.page.fill(self.current_address, current_address)
        self.page.fill(self.permanent_address, permanent_address)
        
    def enviar_formulario(self):
        self.page.click(self.submit_button)
        
        
