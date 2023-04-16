import tkinter
from Timer import Timer
from ui import login_view

class MainView:
    # Luokka joka määrittää sovelluksen näkymän kirjautumisen jälkeen
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.timer = None
        self.study_time = 25
        self.break_time = 5
        self.main_frame = tkinter.Frame(root, width=600, height=600, bg='#FFFFFF')
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.timer_settings_opened = False

    def init_main_view(self):
        # Ulos kirjautumista varten painike
        logout_button = tkinter.Button(master=self.main_frame, text="Log out", command=self._logout, bg='#f55656', activebackground='#f26868')
        logout_button.grid(row=5, column=0, columnspan=3, padx=5, pady=10)

        # Ajastin
        timer_text = f"Study {self.study_time:02d}:00"
        self.time_label = tkinter.Label(master=self.main_frame, text=timer_text, bg='#FFFFFF')
        self.time_label.grid(row=6, column=0, columnspan=3, padx=5, pady=10)

        # Ajastimen toiminnot
        self.timer = None
        self.start_timer = tkinter.Button(master=self.main_frame, text="Start", command=self._start_timer, bg='#FFFFFF')
        self.pause_timer = tkinter.Button(master=self.main_frame, text="Pause", command=self._pause_timer, bg='#FFFFFF')
        self.reset_timer = tkinter.Button(master=self.main_frame, text="Reset", command=self._reset_timer, bg='#FFFFFF')
        timer_button = tkinter.Button(master=self.main_frame, text="Timer Settings", command=self._timer_settings, bg='#FFFFFF')
        self.start_timer.grid(row=7, column=0, padx=5, pady=10)
        self.pause_timer.grid(row=7, column=1, padx=5, pady=10)
        self.reset_timer.grid(row=7, column=2, padx=5, pady=10)
        timer_button.grid(row=8, column=0, columnspan=3, padx=5, pady=10)

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
        close_button = tkinter.Button(master=self.setting_window, text="Go back", command=self.setting_window.destroy, bg='#FFFFFF')
        submit_button.grid(row=2, column=0, padx=5, pady=10)
        close_button.grid(row=2, column=1, padx=5, pady=10)

    def _update_times(self):
        # Päivittää käyttäjän valitsemat ajat ja lataa ajastin näkemymän uudelleen
        self.study_time = self.new_study_time.get()
        self.break_time = self.new_break_time.get()
        # Tuhotaan ikkuna ja päivitetään timer_settings, jotta voi avata uuden.
        self.setting_window.destroy()
        self.timer_settings_opened = False
        # Ladataan päänäkymä
        self.init_main_view()

    def _start_timer(self):
        if self.timer: # Ei luoda uutta ajastinta, jos sellainen olemassa
            return
        else:
            self.timer = Timer(self.study_time, self.break_time)
            self.timer.start()
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
            self.pause_timer.config(text="Pause")
            self.time_label.config(text=f"Study {self.study_time:02d}:00")
        else:
            return

         
    def _update_time_label(self):
        # Päivittää time_labelin tekstiä ja saa jäljellä olevan ajan ajastinluokan countdown() metodista
        if self.timer:
            remaining_time = self.timer.count_down()
            if remaining_time != "00:00" and self.timer.timer_on:
                if self.timer.study_status:
                    label_text = "Study " + remaining_time
                else:
                    label_text = "Break " + remaining_time
                self.time_label.config(text=label_text)
                self.main_frame.after(1000, self._update_time_label)
        return
