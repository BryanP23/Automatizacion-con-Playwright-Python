# pages/formulario_page.py
class FormularioPage:
    def __init__(self, page):
        self.page = page
        self.name_input = "id=firstName"
        self.last_name_input = "id=lastName"
        self.email_input = "id=userEmail"
        self.gender_button = "label[for='gender-radio-1']"
        self.mobile_input = "id=userNumber"
        self.date_of_birth_input = "id=dateOfBirthInput"
        self.subjects_input = "id=subjectsInput"
        self.select_hobbies = "label[for='hobbies-checkbox-2']"
        self.input_file = "id=uploadPicture"
        self.current_address_input = "id=currentAddress"
        self.state_dropdown = "#state"
        self.state_option = "//div[text()='NCR']"
        self.city_dropdown = "#city"
        self.city_option = "//div[text()='Delhi']"
        self.submit_button = "id=submit"
        self.success_modal = "div.modal-content"   # modal de éxito

    def llenar_fecha_nacimiento(self, anio, mes, dia):
        self.page.click(self.date_of_birth_input)
        self.page.select_option(".react-datepicker__year-select", str(anio))
        self.page.select_option(".react-datepicker__month-select", str(mes))  
        self.page.click(f".react-datepicker__day--0{dia:02d}")  # día con 2 dígitos

    def llenar_formulario(self, nombre, apellido, email, movil, materias, archivo, direccion_actual):
        self.page.fill(self.name_input, nombre)
        self.page.fill(self.last_name_input, apellido)
        self.page.fill(self.email_input, email)
        self.page.click(self.gender_button)
        self.page.fill(self.mobile_input, movil)
        self.page.fill(self.subjects_input, materias)
        self.page.keyboard.press("Enter")  # confirmar materia
        self.page.click(self.select_hobbies)
        self.page.set_input_files(self.input_file, archivo)
        self.page.fill(self.current_address_input, direccion_actual)
        self.page.click(self.state_dropdown)
        self.page.click(self.state_option)
        self.page.click(self.city_dropdown)
        self.page.click(self.city_option)

    def enviar_formulario(self):
        self.page.click(self.submit_button)
        self.page.wait_for_selector(self.success_modal)
