class HomePage:
    def __init__(self, page):
        self.page = page
        self.form_button = "xpath=//div[@class='home-body']//div[2]//div[1]//div[2]//*[name()='svg']"   # botón que lleva al formulario
        self.practice_form = "xpath=//span[normalize-space()='Practice Form']"  # botón que lleva al formulario
        
        self.element_button = "xpath=//div[@class='category-cards']//div[1]//div[1]//div[2]//*[name()='svg']"  # botón que lleva a elements
        self.text_box = "//span[normalize-space()='Text Box']"  # botón que lleva al text box
        self.check_box = "//span[normalize-space()='Check Box']" # botón que lleva al check box
        
        # Reto checkbox de datatables localizadores
        self.text_extension = "xpath=//a[normalize-space()='Extensions']"
        self.text_select = "xpath=//a[normalize-space()='Select']"
        self.text_examples = "xpath=//a[@href='/extensions/select/examples']"
        self.text_Disabling_the_header_checkbox = "xpath=//a[normalize-space()='Disabling the header checkbox']"

    def go_to_formulario(self):
        self.page.click(self.form_button)
        self.page.wait_for_url("https://demoqa.com/forms")  # espera hasta que cargue la URL
        self.page.click(self.practice_form)  # clic en el botón del formulario
    def go_to_formularioSencillo(self):
        self.page.click(self.element_button)
        self.page.wait_for_url("https://demoqa.com/elements")  # espera hasta que cargue la URL
        self.page.click(self.text_box)  # clic en el botón del text box
        
    def go_to_checkBox(self):
        self.page.click(self.element_button)
        self.page.wait_for_url("https://demoqa.com/elements")  # espera hasta que cargue la URL
        self.page.click(self.check_box)  # clic en el botón del check box
        
    def go_to_RetoCheckBox(self):
        self.page.click(self.text_extension)
        self.page.click(self.text_select)
        self.page.click(self.text_examples) 
        self.page.click(self.text_Disabling_the_header_checkbox)    
        self.page.wait_for_url("https://datatables.net/extensions/select/examples/checkbox/header.html")  # espera hasta que cargue la URL
        
        
        
        