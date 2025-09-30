import os
from pages.home_page import HomePage
from pages.formulario_page import FormularioPage

def test_llenar_formulario(page):
    home = HomePage(page)
    home.go_to_formulario()

    formulario = FormularioPage(page)
    formulario.llenar_formulario(
        nombre="Bryan",
        apellido="Polo",
        email="bryan@test.com",
        movil="3216549870",
        materias="Astrologia",
        archivo = os.path.join(os.path.dirname(__file__), "..", "Recursos", "Imagen de prueba.png"), 
        # Ruta relativa al archivo de prueba
        # __file__ = ruta completa del archivo actual (ej: .../pages/formulario_page.py)
        # os.path.dirname(__file__) = obtiene solo la carpeta donde está ese archivo (ej: .../pages)
        # Armamos la ruta a la imagen de forma dinámica y portable
        #archivo = os.path.join(
        #os.path.dirname(__file__),  # carpeta actual (pages/)
        #"..",                       # sube un nivel (a Curso/)
        #"Recursos",                 # carpeta donde está la imagen
        #"Imagen de prueba.png"      # nombre del archivo
    
        direccion_actual="Mi dirección en Medallo Morrr"
    )

    formulario.llenar_fecha_nacimiento(1996, 10, 23)  # Noviembre (mes 10 → noviembre) siempre se le resta 1 al mes. si noviembre es 11, se debe usar 10
    formulario.enviar_formulario()

#tomar Foto
    page.screenshot(path="Imagenes/formulario.png")
