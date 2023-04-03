import tkinter
from ui import login_view

class MainView:
    # Luokka joka määrittää sovelluksen näkymän kirjautumisen jälkeen
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.main_frame = tkinter.Frame(root, width=600, height=600, bg='#FFFFFF')
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")
        main_label = tkinter.Label(master=self.main_frame, text="Main App", bg='#FFFFFF')
        main_label.grid(row=0, column= 0, padx=5, pady=5)

    def init_main_view(self):
        # Tällä hetkellä näkymässä vain ulos kirjautumista varten painike
        logout_button = tkinter.Button(master=self.main_frame, text="Log out", command=self._logout, bg='#f55656', activebackground='#f26868')
        logout_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

    def _logout(self):
        # Lataa kirjatumisnäkymän kun käyttäjä kirjautuu ulos
        self.main_frame.destroy()
        self.root = login_view.LoginView(self.root)
        self.root.init_login_form()
