import tkinter
import tkinter.messagebox as messagebox
import User
from ui import register_view, main_view
from repositories import user_repo

class LoginView:
    # Luokka joka määrittää kirjautumisnäkymän
    def __init__(self, root):
        self.root = root
        self.login_frame = tkinter.Frame(root, width=600, height=600, bg='#FFFFFF')
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")
        login_label = tkinter.Label(master=self.login_frame, text="Login", bg='#FFFFFF')
        login_label.grid(row=0, column= 0, padx=5, pady=5)

    def init_login_form(self):
        # Kirjautumislomake
        self.username_label = tkinter.Label(master=self.login_frame, text="Username", bg='#FFFFFF')
        self.username_entry = tkinter.Entry(master=self.login_frame)
        self.username_label.grid(padx=5, pady=5)
        self.username_entry.grid(row=2, column=0, sticky="ew", padx=20, pady=5)

        self.password_label = tkinter.Label(master=self.login_frame, text="Password", bg='#FFFFFF')
        self.password_entry = tkinter.Entry(master=self.login_frame, show='*')
        self.password_label.grid(padx=5, pady=5)
        self.password_entry.grid(row=4, column=0, sticky="ew", padx=20, pady=5)

        login_button = tkinter.Button(master=self.login_frame, text="Login", command=self._login, bg='#FFFFFF')

        create_user_label = tkinter.Label(master=self.login_frame, text="Don't have an account?", bg='#FFFFFF')
        create_user_button = tkinter.Button(master=self.login_frame, text="Register", command=self._register, bg='#FFFFFF')

        login_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)
        create_user_label.grid(padx=5)
        create_user_button.grid(row=7, column=0, columnspan=2, pady=10)

    def _login(self):
        # Tarkistetaan löytyykö käyttäjä ja täsmääkö salasana
        user = User.User(self.username_entry.get(), self.password_entry.get())
        connection = user_repo.UserRepo()
        check_auth = connection.login_user(user)
        if check_auth == False:
            messagebox.showerror("Error", 'Username or password incorrect')
        else:
            # Kirjautumisen onnistuessa ladataan sovelluksen näkymä
            self.login_frame.destroy()
            self.root = main_view.MainView(self.root, user)
            self.root.init_main_view()

    def _register(self):
        # Lataa rekisteröitymisnäkymän
        self.login_frame.destroy()
        self.root = register_view.RegisterView(self.root)
        self.root.init_register_form()