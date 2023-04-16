import tkinter as tk
from ui import login_view

class App(tk.Tk):
    def __init__(self):
        self.root = tk.Tk.__init__(self)
        self.title('Study Timer')
        self.geometry('500x500')
        self.configure(bg="#FFFFFF")

        # Sovelluksen käynnistyessä renderöidään aina kirjautumisnäkymä
        self._frame = login_view.LoginView(self.root)
        self._frame.init_login_form()


if __name__ == "__main__":
    app = App()
    app.mainloop()
