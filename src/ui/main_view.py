import tkinter
from entities.Timer import Timer
from repositories import todo_repo
from entities import Todo
from services import timer_service
from ui import login_view

class MainView:
    # Luokka joka määrittää sovelluksen näkymän kirjautumisen jälkeen
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.timer = None
        self.timer_service = None
        self.study_time = 25
        self.break_time = 5
        self.main_frame = tkinter.Frame(root, width=600, height=800, bg='#FFFFFF')
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.timer_settings_opened = False

    def init_main_view(self):
        # Ulos kirjautumista varten painike
        logout_button = tkinter.Button(master=self.main_frame, text="Log out", command=self._logout, bg='#f55656', activebackground='#f26868')
        logout_button.grid(row=5, column=0, columnspan=3, pady=10)

        # Ajastin
        timer_text = f"Study {self.study_time:02d}:00"
        self.time_label = tkinter.Label(master=self.main_frame, text=timer_text, bg='#FFFFFF')
        self.time_label.grid(row=6, column=0, columnspan=3, pady=10)

        # Ajastimen toiminnot
        self.timer = None
        self.start_timer = tkinter.Button(master=self.main_frame, width=8, text="Start", command=self._start_timer, bg='#FFFFFF')
        self.pause_timer = tkinter.Button(master=self.main_frame, width=8, text="Pause", command=self._pause_timer, bg='#FFFFFF')
        self.reset_timer = tkinter.Button(master=self.main_frame, width=8, text="Reset", command=self._reset_timer, bg='#FFFFFF')
        timer_button = tkinter.Button(master=self.main_frame, text="Timer Settings", command=self._timer_settings, bg='#FFFFFF')
        self.start_timer.grid(row=7, column=0,padx=5, pady=5, sticky="nsew")
        self.pause_timer.grid(row=7, column=1, pady=5, sticky="nsew")
        self.reset_timer.grid(row=7, column=2, padx=5, pady=5, sticky="nsew")
        timer_button.grid(row=8, column=0, columnspan=3, pady=5, sticky="nsew")

        # Todot
        self.todo_box = tkinter.Listbox(master=self.main_frame, width=50, height=10)
        self.todo_box.grid(row=9, column=0, columnspan=3)
        self.scrollbar = tkinter.Scrollbar(master=self.main_frame, orient="vertical", command=self.todo_box.yview)
        self.scrollbar.configure(width=20, troughcolor="white", bg="#000000", activebackground="grey",borderwidth=0)
        self.scrollbar.grid(row=9, column=3, padx=5)
        self.todo_box.config(yscrollcommand=self.scrollbar.set)

        # TodoReposta haetaan kaikki käyttäjän todot.
        connection = todo_repo.TodoRepo()
        todos = connection.get_user_todos(self.user)
        for todo in todos:
            self.todo_box.insert("end", todo[0])

        # Todo toiminnot
        self.new_todo = tkinter.Text(master=self.main_frame, height=2, width=30, pady=5)
        self.create_todo = tkinter.Button(master=self.main_frame, text="Create Todo", command=self._create_todo, bg='#FFFFFF')
        self.del_todo = tkinter.Button(master=self.main_frame, text="Delete Selected", command=self._delete_todo, bg='#FFFFFF')
        self.new_todo.grid(row=10, column=0, columnspan=2, padx=5, pady=10)
        self.create_todo.grid(row=10, column=2, columnspan=1, padx=5, pady=10)
        self.del_todo.grid(row=11, column=0, columnspan=3, padx=5, pady=10)

    def _create_todo(self):
        # Tallentaa uuden todon tietokantaan ja päivittää sen käyttöliittymään
        todo_to_save = Todo.Todo(self.user, self.new_todo.get("1.0", "end-1c"), False)
        self.new_todo.delete("1.0", "end-1c")
        connection = todo_repo.TodoRepo()
        connection.create_todo(self.user, todo_to_save)
        self.todo_box.insert("end", todo_to_save.content)
    
    def _delete_todo(self):
        # Poistaa valitun todon tietokannasta ja käyttöliittymästä
        selection = self.todo_box.curselection()
        todo_to_delete = self.todo_box.get(selection[0])
        connection = todo_repo.TodoRepo()
        connection.delete_todo(self.user, todo_to_delete)
        self.todo_box.delete(tkinter.ANCHOR)

    def _logout(self):
        # Lataa kirjatumisnäkymän kun käyttäjä kirjautuu ulos
        self.main_frame.destroy()
        self.root = login_view.LoginView(self.root)
        self.root.init_login_form()

    def _timer_settings(self):
        # Ei avata uutta ikkunaa jos ikkuna on auki
        if self.timer_settings_opened:
            return
        self.timer_settings_opened = True
        # Toplevel tkinter widget, jossa voi määrittää ajat
        self.setting_window = tkinter.Toplevel(self.root, bg="#FFFFFF")
        self.setting_window.geometry("270x170")
        self.setting_window.title("Timer Settings")
        self.setting_window.resizable(False, False)

        study_time_label = tkinter.Label(master=self.setting_window, text="Study time", bg='#FFFFFF')
        self.new_study_time = tkinter.Scale(master=self.setting_window, from_=10, to=120, orient="horizontal", bg='#FFFFFF')
        break_time_label = tkinter.Label(master=self.setting_window, text="Break time", bg='#FFFFFF')
        self.new_break_time = tkinter.Scale(master=self.setting_window, from_=5, to=120, orient="horizontal", bg='#FFFFFF')
        study_time_label.grid(row=0, column=0, padx=5, pady=10)
        self.new_study_time.grid(row=0, column=1, padx=5, pady=10)
        break_time_label.grid(row=1, column=0, padx=5, pady=10)
        self.new_break_time.grid(row=1, column=1, padx=5, pady=10)

        submit_button = tkinter.Button(master=self.setting_window, text="Set times", command=self._update_times, bg='#FFFFFF')
        close_button = tkinter.Button(master=self.setting_window, text="Go back", command=self._close_timer_settings, bg='#FFFFFF')
        submit_button.grid(row=2, column=0, padx=5, pady=10)
        close_button.grid(row=2, column=1, padx=5, pady=10)

    def _close_timer_settings(self):
        self.setting_window.destroy()
        self.timer_settings_opened = False


    def _update_times(self):
        # Päivittää käyttäjän valitsemat ajat ja lataa ajastin näkemymän uudelleen
        self.study_time = self.new_study_time.get()
        self.break_time = self.new_break_time.get()
        # Tuhotaan ikkuna ja päivitetään timer_settings, jotta voi avata uuden.
        self.setting_window.destroy()
        self.timer_settings_opened = False
        # Ladataan päänäkymä
        self.pause_timer.config(text="Pause")
        self.init_main_view()

    def _start_timer(self):
        if self.timer: # Ei luoda uutta ajastinta, jos sellainen olemassa
            return
        else:
            self.timer = Timer(self.study_time, self.break_time)
            self.timer_service = timer_service.TimerService(self.timer)
            self.timer_service.start()
            self._update_time_label()

    def _pause_timer(self):
        # Metodi joka mahdollistaa ajastimen tauko toiminnallisuuden, toimii vain jos ajastin olemassa
        if self.timer:
            self.timer.timer_on = not self.timer.timer_on
            if self.timer.timer_on:
                self.pause_timer.config(text=" Pause ")
                # Ajastin taas päällä, niin päivitetään timer_label
                self._update_time_label()
            else:
                self.pause_timer.config(text="Continue")
        return

    def _reset_timer(self):
        # Resetoi ajastimen, poistamalla olemassa olevan
        if self.timer:
            self.timer = None
            self.timer_service = None
            self.pause_timer.config(text="Pause")
            self.time_label.config(text=f"Study {self.study_time:02d}:00")
        else:
            return

         
    def _update_time_label(self):
        # Päivittää time_labelin tekstiä ja saa jäljellä olevan ajan ajastinluokan countdown() metodista
        if self.timer:
            remaining_time = self.timer_service.count_down()
            if remaining_time != "00:00" and self.timer.timer_on:
                if self.timer.study_status:
                    label_text = "Study " + remaining_time
                else:
                    label_text = "Break " + remaining_time
                self.time_label.config(text=label_text)
                self.main_frame.after(1000, self._update_time_label)
        return
