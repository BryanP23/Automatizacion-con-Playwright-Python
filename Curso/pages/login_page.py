
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = "#username"
        self.password_input = "#password"
        self.login_button = "#login"

    def navigate(self, base_url):
        self.page.goto(f"{base_url}/login")

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
