import pytest
from playwright.sync_api import sync_playwright

# 🔹 Registrar las opciones personalizadas de pytest.ini
def pytest_addoption(parser):
    parser.addini("demoqa_url", "Base URL para DemoQA")
    parser.addini("datatables_url", "Base URL para DataTables")
    parser.addini("google_url", "Base URL para Google")

# ✅ Fixture para lanzar el browser una sola vez en la sesión
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        # ⚙️ Configuración del navegador
        browser = p.chromium.launch(
            headless=False,   # False = abre la ventana del navegador (útil para ver la prueba)
            slow_mo=2000    # Espera de 2000 ms entre cada acción (más lento y visible) entre mas alto el número, más lento (útil para ver la prueba)
        )
        yield browser
        browser.close()
        
# ✅ Fixture con URLs centralizadas (del pytest.ini)
@pytest.fixture(scope="session")
def urls(pytestconfig):
    return {
        "demoqa": pytestconfig.getini("demoqa_url"),
        "datatables": pytestconfig.getini("datatables_url"),
        "google": pytestconfig.getini("google_url"),
    }

# ✅ Fixture principal que crea la "page" para cada test
@pytest.fixture
def page(browser):
# 🎥 Creamos un contexto con grabación de video activada
# 📌 IMPORTANTE: Aquí es donde se activa la grabación
    context = browser.new_context(
        record_video_dir="videos/",               # Carpeta donde se guardan los videos
        record_video_size={"width": 1280, "height": 720}  # Resolución de la grabación, si quiero mas resolución, aumentar estos valores
    )
    # si quiero desactivar la grabación, comento las líneas de record_video_dir y record_video_size

    # 📝 Nueva pestaña
    page = context.new_page()
    
    
 # 🚀 Script global para resaltar clics con un círculo espandible rojo
    page.add_init_script("""
        (() => {
            document.addEventListener('mousedown', e => {
                const circle = document.createElement('div');
                circle.style.position = 'absolute';
                circle.style.width = '30px';
                circle.style.height = '30px';
                circle.style.border = '2px solid red';
                circle.style.borderRadius = '50%';
                circle.style.left = (e.pageX - 15) + 'px';
                circle.style.top = (e.pageY - 15) + 'px';
                circle.style.pointerEvents = 'none';
                circle.style.zIndex = 9999;
                circle.style.opacity = '0.8';
                circle.style.transition = 'transform 0.4s ease-out, opacity 0.4s ease-out';
                document.body.appendChild(circle);

                requestAnimationFrame(() => {
                    circle.style.transform = 'scale(2)';
                    circle.style.opacity = '0';
                });

                setTimeout(() => circle.remove(), 400);
            });
        })();
    """)

    # 🔄 Retornar la página al test
    yield page

    # ❌ Cerramos el contexto (esto guarda y finaliza el video)
    context.close()
    
    


