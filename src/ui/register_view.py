import tkinter
import tkinter.messagebox as messagebox
import entities.User as User
from repositories import user_repo
from ui import login_view

class RegisterView:
    # Luokka joka määrittää rekisteröitymisnäkymän
    def __init__(self, root):
        self.root = root
        self.register_frame = tkinter.Frame(root, width=600, height=800, bg='#FFFFFF')
        self.register_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.register_label = tkinter.Label(master=self.register_frame, text="Register", bg='#FFFFFF')
        self.register_label.grid(row=0, column= 0, padx=5, pady=5)


    def init_register_form(self):
        # Rekisteröitymislomake
        self.username_label = tkinter.Label(master=self.register_frame, text="Username", bg='#FFFFFF')
        self.username_entry = tkinter.Entry(master=self.register_frame)
        self.username_label.grid(padx=5, pady=5)
        self.username_entry.grid(row=2, column=0, sticky="ew", padx=20, pady=5)

        self.password_label = tkinter.Label(master=self.register_frame, text="Password", bg='#FFFFFF')
        self.password_entry = tkinter.Entry(master=self.register_frame, show='*')
        self.password_label.grid(padx=5, pady=5)
        self.password_entry.grid(row=4, column=0, sticky="ew", padx=20, pady=5)

        self.second_password_label = tkinter.Label(master=self.register_frame, text="Password second time", bg='#FFFFFF')
        self.second_password_entry = tkinter.Entry(master=self.register_frame, show='*')
        self.second_password_label.grid(padx=5, pady=5)
        self.second_password_entry.grid(row=6, column=0, sticky="ew", padx=20, pady=5)

        submit_button = tkinter.Button(master=self.register_frame, text="Register", command=self._handle_registration, bg='#FFFFFF')
        submit_button.grid(row=7, column=0, columnspan=2, padx=5, pady=10)

        go_back_button = tkinter.Button(master=self.register_frame, text="Back to login", command=self._back_to_login, bg='#FFFFFF')
        go_back_button.grid(row=8, column=0, columnspan=2, padx=5, pady=10)

    def _handle_registration(self):
        # Metodi joka tarkistaa ensin täsmääkö salasanat ja tallentaa käyttäjän tietokantaan.
        if self.password_entry.get() == self.second_password_entry.get():
            new_user = User.User(self.username_entry.get(), self.password_entry.get())
            users = user_repo.UserRepo()
            save_to_db = users.register_user(new_user)
            if save_to_db == False:
                messagebox.showerror("Error", 'Username taken')
            else:
                # Takaisin kirjautumisnäkymään
                self._back_to_login()
        else:
            # Jos salasanat eivät täsmää
            messagebox.showerror("Error", 'Passwords not matching')
    
    def _back_to_login(self):
        # Lataa kirjautumisnäkymän
        self.register_frame.destroy()
        self.root = login_view.LoginView(self.root)
        self.root.init_login_form()