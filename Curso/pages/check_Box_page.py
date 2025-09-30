import time
from playwright.sync_api import expect

class CheckBoxPage:
    def __init__(self, page):

        # Establecer un tiempo de espera predeterminado
        #page.set_default_timeout(5000)
        self.page = page
        self.Chevron_right_Home = "xpath=//*[name()='path' and contains(@d,'M10 6L8.59')]"
        self.chevron_right_Documents = "xpath=//li[2]//span[1]//button[1]//*[name()='svg']//*[name()='path' and contains(@d,'M10 6L8.59')]"
        self.chevron_right_Office = "xpath=//body//div[@id='app']//li[@class='rct-node rct-node-parent rct-node-expanded']//li[@class='rct-node rct-node-parent rct-node-expanded']//li[2]//span[1]//button[1]//*[name()='svg']//*[name()='path' and contains(@d,'M10 6L8.59')]"
        self.select_Box_classified = "xpath=//label[@for='tree-node-classified']//span[@class='rct-checkbox']//*[name()='svg']"
        
        
    def seleccionar_checkBox(self):
        # Esperar que esté visible antes de seleccionar         
        expect(self.page.locator(self.Chevron_right_Home)).to_be_visible()  # Esperar a que el campo de nombre sea visible
        self.page.click(self.Chevron_right_Home)
        expect(self.page.locator(self.chevron_right_Documents)).to_be_visible()  # Esperar a que el campo de email sea visible
        self.page.click(self.chevron_right_Documents)               
        expect(self.page.locator(self.chevron_right_Office)).to_be_visible()  # Esperar a que el campo de email sea visible
        self.page.click(self.chevron_right_Office)
        expect(self.page.locator(self.select_Box_classified)).to_be_visible()  # Esperar a que el campo de email sea visible
        self.page.click(self.select_Box_classified) 
        
        self.result = "xpath=//span[@class='text-success']"
        
        
        