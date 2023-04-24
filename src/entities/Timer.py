class Timer:
    # Luokka joka määrittää ajastimen.
    def __init__(self, study, rest):
        self.study_status = True
        self.study = study*60
        self.rest = rest*60
        self.remaining_time = 0
        self.timer_on = False
