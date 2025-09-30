| Acción                    | Método                                           | Ejemplo                                                          | Descripción                       |
| ------------------------- | ------------------------------------------------ | ---------------------------------------------------------------- | --------------------------------- |
| **Navegar**               | `goto(url)`                                      | `await page.goto("https://demoqa.com")`                          | Abre una página.                  |
| **Escribir texto**        | `fill(selector, text)`                           | `await page.fill("#firstName", "Bryan")`                         | Borra lo que hay y escribe.       |
| **Escribir como humano**  | `type(selector, text, delay=100)`                | `await page.type("#firstName", "Bryan", delay=100)`              | Escribe con retraso entre teclas. |
| **Presionar tecla**       | `press(selector, key)`                           | `await page.press("#input", "Enter")`                            | Simula pulsar teclas.             |
| **Clic**                  | `click(selector)`                                | `await page.click("button#submit")`                              | Hace clic en un botón/enlace.     |
| **Doble clic**            | `dblclick(selector)`                             | `await page.dblclick("text=Editar")`                             | Doble clic.                       |
| **Hover**                 | `hover(selector)`                                | `await page.hover("text=Menú")`                                  | Pasa el mouse encima.             |
| **Checkbox (marcar)**     | `check(selector)`                                | `await page.check("#accept")`                                    | Marca un checkbox.                |
| **Checkbox (desmarcar)**  | `uncheck(selector)`                              | `await page.uncheck("#accept")`                                  | Desmarca un checkbox.             |
| **Seleccionar opción**    | `select_option(selector, value/label/index)`     | `await page.select_option("#state", "NCR")`                      | Selecciona en un `<select>`.      |
| **Subir archivo**         | `set_input_files(selector, file)`                | `await page.set_input_files("#upload", "C:/cv.pdf")`             | Sube un archivo.                  |
| **Obtener texto**         | `inner_text(selector)`                           | `msg = await page.inner_text("h1")`                              | Obtiene el texto visible.         |
| **Obtener HTML**          | `inner_html(selector)`                           | `html = await page.inner_html("#div")`                           | Obtiene el HTML interno.          |
| **Obtener atributo**      | `get_attribute(selector, attr)`                  | `val = await page.get_attribute("#email", "value")`              | Lee un atributo.                  |
| **Esperar elemento**      | `wait_for_selector(selector)`                    | `await page.wait_for_selector("text=Gracias")`                   | Espera hasta que aparezca.        |
| **Esperar URL**           | `wait_for_url(url)`                              | `await page.wait_for_url("**/home")`                             | Espera a que la URL cambie.       |
| **Esperar carga**         | `wait_for_load_state("networkidle")`             | `await page.wait_for_load_state("networkidle")`                  | Espera que la red esté inactiva.  |
| **Scroll hasta elemento** | `locator(selector).scroll_into_view_if_needed()` | `await page.locator("text=Enviar").scroll_into_view_if_needed()` | Hace scroll hasta el elemento.    |
| **Recargar página**       | `reload()`                                       | `await page.reload()`                                            | Recarga la página actual.         |
| **Atrás / Adelante**      | `go_back()` / `go_forward()`                     | `await page.go_back()`                                           | Navegación del historial.         |
| **Captura de pantalla**   | `screenshot(path="archivo.png")`                 | `await page.screenshot(path="form.png")`                         | Guarda screenshot.                |
| **Guardar PDF**           | `pdf(path="archivo.pdf")`                        | `await page.pdf(path="page.pdf")`                                | Guarda como PDF (solo Chromium).  |
