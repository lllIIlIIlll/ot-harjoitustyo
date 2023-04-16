import pygame

class Timer:
    # Luokka joka määrittää ajastimen.
    def __init__(self, study, rest):
        self.study_status = True
        self.study = study*60
        self.rest = rest*60
        self.remaining_time = 0
        self.timer_on = False
        pygame.mixer.init()

    def count_down(self):
        if self.remaining_time <= 0:
            if self.study_status is True:
                self.remaining_time = self.rest
                self.study_status = False
                self.play_status_change()
                self.start()
            else:
                self.remaining_time = self.study
                self.study_status = True
                self.play_status_change()
                self.start()

        minutes, seconds = divmod(self.remaining_time, 60)
        # Päivitetään jäljellä olevaa aikaa vain jos ajastin käynnissä.
        if self.timer_on:
            self.remaining_time -= 1

        return f"{minutes:02d}:{seconds:02d}"

    def start(self):
        # Jos ajastin on käynnissä ei aloiteta uutta.
        if self.timer_on:
            return
        self.timer_on = True
        if self.study_status:
            self.remaining_time = self.study
        else:
            self.remaining_time = self.rest

        self.play_status_change()
        self.count_down()

    def play_status_change(self):
        sound = pygame.mixer.Sound("sounds/sound.mp3")
        sound.play()
