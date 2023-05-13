import unittest
from entities import Timer
from services import timer_service

class TestTimerService(unittest.TestCase):
    def setUp(self):
        self.timer = Timer.Timer(1, 1)
        self.timer_services = timer_service.TimerService(self.timer)
        
    def test_duplicate_timer(self):
        self.timer_services.start()
        timer_to_test = self.timer_services.start()
        self.assertEqual(timer_to_test, False)