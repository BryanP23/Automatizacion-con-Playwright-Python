✅ Esperas y validaciones en Playwright

Cuando interactuamos con un elemento (ej: .fill(), .click()), es buena práctica asegurarnos de que esté disponible en la página.

1. expect (validación explícita)

Verifica que el elemento esté visible antes de usarlo:

from playwright.sync_api import expect

expect(page.locator("#firstName")).to_be_visible()
page.fill("#firstName", "Bryan")

2. wait_for_selector (espera manual)

Espera a que un elemento cumpla un estado:

page.wait_for_selector("#firstName", state="visible")
page.fill("#firstName", "Bryan")


Estados disponibles:

"attached" → existe en el DOM

"visible" → aparece en pantalla

"hidden" → está oculto

"detached" → fue removido

3. Uso directo de locator() (auto-wait integrado)

Playwright ya espera automáticamente a que el elemento esté visible y listo para interactuar:

page.locator("#firstName").fill("Bryan")

⚡ Resumen

Usa expect → si quieres validar explícitamente.

Usa wait_for_selector → si necesitas control preciso.

Usa locator() directamente → sencillo y seguro (Playwright espera por ti).

| Método              | 📝 Descripción                                        | 🛠️ Ejemplo                                      |
| ------------------- | ----------------------------------------------------- | ------------------------------------------------ |
| `expect`            | Valida que un elemento esté visible, habilitado, etc. | `expect(page.locator("#id")).to_be_visible()`    |
| `wait_for_selector` | Espera un estado específico del elemento              | `page.wait_for_selector("#id", state="visible")` |
| `locator()`         | Playwright espera automáticamente                     | `page.locator("#id").click()`                    |
