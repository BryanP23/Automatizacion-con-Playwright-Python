# 🚀 Automatización con Playwright + Python  

Este proyecto contiene diferentes **automatizaciones de pruebas web** desarrolladas con **Playwright y Python**, enfocadas en **formularios, logins, interacciones con checkboxes, tablas dinámicas y flujos completos en sitios reales**.  

Mi objetivo es **aprender, practicar y demostrar habilidades en QA Automation**, creando un repositorio organizado, escalable y con ejemplos claros que puedan ser útiles para **otros testers, estudiantes y reclutadores**.  

---

## 📌 Tecnologías utilizadas  
- 🐍 **Python 3.12**  
- 🎭 **Playwright**  
- ✅ **Pytest** (para la ejecución de pruebas)  
- 🛠 **OS y Pathlib** (para manejo de rutas y recursos)  

---

## 🌐 Sitios web automatizados hasta el momento  
- [DemoQA](https://demoqa.com/) → Formularios, logins, checkboxes, subida de archivos.  
- [DataTables](https://datatables.net/) → Filtrado, ordenamiento y validación de datos en tablas dinámicas.  
- Sitios de práctica adicionales (logins, formularios y validaciones).  
- Próximamente → **Automatización de una compra real en [Mattelsa](https://www.mattelsa.net/)** 🛒.  

---

## 📂 Estructura del proyecto  
```bash
Proyecto-con-Playwright/
│
├── Curso/                   
│   ├── Ejemplos/             # Ejemplos de pruebas (material extra de práctica)
│   ├── Imagenes/             # Screenshots generados en las pruebas
│   ├── pages/                # Page Object Models (POM)
│   ├── playwright_env/       # Entorno/archivos relacionados a Playwright
│   ├── Recursos/             # Archivos de apoyo (ej: imágenes para upload)
│   ├── tests/                # Casos de prueba automatizados
│   │   ├── conftest.py       # Configuración global de pytest
│   │   ├── test_checkbox.py  
│   │   ├── test_formulario.py
│   │   ├── test_formularioSencillo.py
│   │   ├── test_login.py
│   │   ├── test_Reto_CheckBoxAleatorio.py
│   │   └── testexample.py
│   ├── videos/               # Grabaciones en video de las ejecuciones
│   ├── pytest.ini            # Configuración de pytest
│   ├── requirements.txt      # Dependencias del proyecto
│   └── README.md             # Documentación del proyecto

⚡ Cómo ejecutar el proyecto

Clonar el repositorio:

git clone https://github.com/tu-usuario/Proyecto-con-Playwright.git
cd Proyecto-con-Playwright/Curso


Instalar dependencias:

pip install -r requirements.txt


Ejecutar pruebas:

pytest -v


O para ejecutar en navegador con UI:

pytest --headed

🎯 Objetivo del proyecto

Practicar y consolidar mis conocimientos en QA Automation.

Mostrar buenas prácticas en la organización de proyectos y el uso de Playwright con Python.

Ampliar el proyecto hacia casos más complejos como e-commerce, validación de datos y pruebas end-to-end.

📌 Próximos pasos

✅ Más formularios complejos.

✅ Manejo avanzado de tablas dinámicas.

🛒 Flujo de compra en Mattelsa.

🔗 Integración con CI/CD (GitHub Actions).

📊 Reportes de pruebas más completos (Allure u otros).

✨ Autor

👨‍💻 Bryan Polo
🔗 LinkedIn
https://www.linkedin.com/in/bryanpolo/







