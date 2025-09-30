class listaDinamica_page:
    def __init__(self, page):
        self.page = page
        self.search_input = "id=APjFqb" # input de búsqueda de Google
        
    def buscar_auto(self): 
        
        self.page.click(self.search_input)  
        self.page.fill(self.search_input, "volkswagen jetta gli") # escribir en el input
        self.page.click(self.search_input)
        self.volkswagen_2025 = "xpath=//span[normalize-space()='volkswagen jetta gli']" # opción del autocompletar
        self.page.click(self.volkswagen_2025)  # seleccionar la opción del autocompletar
