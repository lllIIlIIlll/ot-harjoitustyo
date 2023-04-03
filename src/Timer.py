import time

class Timer:
    # Luokka joka määrittää ajastimen
    def __init__(self, study, rest):
        self.study = study
        self.rest = rest

    def count_down(self, remaining):
        while remaining > 0:
            minutes, seconds = divmod(remaining, 60)
            print(minutes, 'min', seconds, 's',end='\r')
            time.sleep(1)
            remaining -= 1
    
    def start(self):
        while True:
            print('Study time')
            self.count_down(self.study)
            print('Break')
            self.count_down(self.rest)  


#timer = Timer(1*60, 1*60)
#timer.start()