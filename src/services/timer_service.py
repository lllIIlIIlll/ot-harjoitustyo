import pygame

class TimerService:
    # Luokka joka määrittää ajastimen.
    def __init__(self, timer):
        self.timer = timer
        pygame.mixer.init()

    def count_down(self):
        if self.timer.remaining_time <= 0:
            if self.timer.study_status is True:
                self.timer.remaining_time = self.timer.rest
                self.timer.study_status = False
                self.play_status_change()
                self.start()
            else:
                self.timer.remaining_time = self.timer.study
                self.timer.study_status = True
                self.play_status_change()
                self.start()

        minutes, seconds = divmod(self.timer.remaining_time, 60)
        # Päivitetään jäljellä olevaa aikaa vain jos ajastin käynnissä.
        if self.timer.timer_on:
            self.timer.remaining_time -= 1

        return f"{minutes:02d}:{seconds:02d}"

    def start(self):
        # Jos ajastin on käynnissä ei aloiteta uutta.
        if self.timer.timer_on:
            return
        self.timer.timer_on = True
        if self.timer.study_status:
            self.timer.remaining_time = self.timer.study
        else:
            self.timer.remaining_time = self.timer.rest

        self.play_status_change()
        self.count_down()

    def play_status_change(self):
        sound = pygame.mixer.Sound("sounds/sound.mp3")
        sound.play()
